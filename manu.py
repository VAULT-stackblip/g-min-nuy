import time
import flet as ft

def main(page: ft.Page):
    page.title = "G-Min-Nuy Mobile"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0D0B12"
    page.window_width = 380
    page.window_height = 700
    page.window_resizable = False

    # ฟังก์ชันตรวจสอบคีย์
    def verify_key(entered_key):
        valid_keys = {
            "VIP-LIFETIME-01": "คีย์ถาวร (Lifetime)",
            "VIP-30DAYS-01": "คีย์ 30 วัน",
            "VIP-07DAYS-01": "คีย์ 7 วัน",
            "VIP-01DAY-01": "คีย์ 1 วัน",
        }
        if entered_key in valid_keys:
            return True, "[+] ตรวจสอบคีย์สำเร็จ!", valid_keys[entered_key]
        elif entered_key == "BOSS":  # คีย์เทสด่วน
            return True, "[+] เปิดใช้งานโหมดแอดมิน!", "VIP ถาวร"
        return False, "[-] คีย์ไม่ถูกต้องหรือหมดอายุ!", None

    def show_dashboard(key_type):
        page.clean()

        def create_feature_row(title_text, subtitle_text, icon_name):
            switch = ft.Switch(value=False, active_color="#9C27B0")
            return ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(name=icon_name, color="#C084FC", size=24),
                        ft.VerticalDivider(width=10),
                        ft.Column(
                            [
                                ft.Text(title_text, size=14, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                                ft.Text(subtitle_text, size=10, color="#9CA3AF"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=1,
                            expand=True
                        ),
                        switch,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=10,
                bgcolor="#161224",
                border_radius=10,
                border=ft.border.all(1, "#7E22CE"),
                margin=ft.margin.symmetric(vertical=4)
            )

        start_button = ft.ElevatedButton(
            text="START GAME",
            icon=ft.icons.PLAY_ARROW_ROUNDED,
            color="#FFFFFF",
            bgcolor="#DC2626",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=12),
            on_click=lambda e: print("[+] เปิดใช้งานฟังก์ชันสำเร็จ!"),
            width=320,
        )

        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("G-Min-Nuy", size=24, weight=ft.FontWeight.BOLD, color="#E9D5FF"),
                        ft.Text(f"Status: Active ({key_type})", size=11, color="#A855F7"),
                        ft.Container(height=10),
                        create_feature_row("ล็อคคอ", "ล็อคเป้าหมายที่คอศัตรูอัตโนมัติ", ft.icons.MY_LOCATION),
                        create_feature_row("ล็อคตัว", "ล็อคเป้าหมายที่ลำตัวแม่นยำสูง", ft.icons.PERSON),
                        create_feature_row("มองทะลุ", "มองเห็นตำแหน่งศัตรูผ่านสิ่งกีดขวาง", ft.icons.VISIBILITY),
                        ft.Container(height=15),
                        start_button,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=15,
                bgcolor="#0F0C1B",
                border_radius=15,
                border=ft.border.all(2, "#9333EA"),
                width=350,
            )
        )
        page.update()

    def show_login():
        page.clean()

        key_input = ft.TextField(
            label="Enter License Key",
            label_style=ft.TextStyle(color="#9CA3AF"),
            border_color="#7E22CE",
            color="#FFFFFF",
            bgcolor="#161224",
            border_radius=10,
            text_align=ft.TextAlign.CENTER,
        )

        status = ft.Text("", size=11, color="#C4C7C5")

        def handle_click(e):
            success, msg, k_type = verify_key(key_input.value.strip())
            if success:
                status.value = msg
                status.color = "#4ADE80"
                page.update()
                time.sleep(0.5)
                show_dashboard(k_type)
            else:
                status.value = msg
                status.color = "#F87171"
                page.update()

        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(name=ft.icons.SECURITY, color="#C084FC", size=48),
                        ft.Text("G-Min-Nuy", size=28, weight=ft.FontWeight.BOLD, color="#E9D5FF"),
                        ft.Text("Mobile License Authentication", size=11, color="#A855F7"),
                        ft.Container(height=20),
                        key_input,
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            text="VERIFY KEY",
                            color="#FFFFFF",
                            bgcolor="#7E22CE",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=12),
                            on_click=handle_click,
                            width=300,
                        ),
                        ft.Container(height=10),
                        status,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                bgcolor="#0F0C1B",
                border_radius=15,
                border=ft.border.all(2, "#9333EA"),
                width=350,
            )
        )
        page.update()

    show_login()

if __name__ == "__main__":
    ft.app(target=main)
