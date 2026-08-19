from __future__ import annotations

import uuid

import allure
import requests

from data import API_URL, DEFAULT_PASSWORD


class StellarApiClient:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.trust_env = False

    @allure.step("Создать пользователя через API")
    def create_user(self) -> dict[str, str]:
        email = f"test_{uuid.uuid4().hex[:12]}@example.com"
        payload = {
            "email": email,
            "password": DEFAULT_PASSWORD,
            "name": "Test User",
        }
        response = self.session.post(f"{API_URL}/auth/register", json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        return {
            "email": email,
            "password": DEFAULT_PASSWORD,
            "access_token": data["accessToken"],
            "refresh_token": data["refreshToken"],
        }

    @allure.step("Удалить пользователя через API")
    def delete_user(self, access_token: str) -> None:
        response = self.session.delete(
            f"{API_URL}/auth/user",
            headers={"Authorization": access_token},
            timeout=15,
        )
        if response.status_code not in (200, 202, 204, 404):
            response.raise_for_status()

    @allure.step("Получить ингредиенты через API")
    def get_ingredients(self) -> list[dict]:
        response = self.session.get(f"{API_URL}/ingredients", timeout=15)
        response.raise_for_status()
        return response.json()["data"]

    @allure.step("Получить ингредиенты для заказа")
    def ingredient_ids_for_order(self) -> list[str]:
        ingredients = self.get_ingredients()
        bun = next(item for item in ingredients if item["type"] == "bun")
        main = next(item for item in ingredients if item["type"] == "main")
        sauce = next(item for item in ingredients if item["type"] == "sauce")
        return [bun["_id"], main["_id"], sauce["_id"]]

    @allure.step("Создать заказ через API")
    def create_order(self, access_token: str) -> int:
        response = self.session.post(
            f"{API_URL}/orders",
            headers={"Authorization": access_token},
            json={"ingredients": self.ingredient_ids_for_order()},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["order"]["number"]
