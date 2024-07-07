import flet as ft


def main(page: ft.Page):
    page.title = "Search set"
    page.add(
        ft.ElevatedButton(text="Start")
    )


ft.app(target=main)