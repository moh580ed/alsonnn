from flet import *
from datetime import datetime 

def create_appbar(root):
    """إنشاء AppBar موحد مع تصميم محسّن"""
    return AppBar(
        title=Text('الأسن للعلوم الحديثة', color=colors.WHITE, size=25, weight=FontWeight.BOLD),
        bgcolor=colors.BLUE_700,
        center_title=True,
        elevation=10,
        leading=Icon(icons.SCHOOL, color=colors.WHITE),
        actions=[
            PopupMenuButton(
                icon=icons.MORE_VERT,
                items=[
                    PopupMenuItem(text="الملف الشخصي", on_click=lambda _: root.go("/الصفحه الراسية")),
                    PopupMenuItem(text="الإعدادات", icon=icons.SETTINGS),
                    PopupMenuItem(text="النتيجة", on_click=lambda _: root.go("/النتيجه"), icon=icons.GRADE),
                    PopupMenuItem(text="الشات", on_click=lambda _: root.go("/الشات"), icon=icons.CHAT),  # إضافة الشات
                    PopupMenuItem(text="الموقع الرسمي", icon=icons.WEB),
                    PopupMenuItem(text="من نحن", icon=icons.INFO),
                    PopupMenuItem(text="المساعدة", on_click=lambda _: root.go("/المساعدة"), icon=icons.HELP),
                ]
            )
        ]
    )

def main(root: Page):
    
    root.title = 'Alson Education'
    root.window.height = 740
    root.window.width = 390
    root.window.top = 10
    root.window.left = 1289
    root.theme_mode = ThemeMode.LIGHT
    root.scroll = "auto"
    root.bgcolor = colors.GREY_100

    
    chat_messages = []

    
    def route_change(route):
        root.views.clear()
        
        
        if root.route == "/":
            root.views.append(
                View(
                    "/",
                    [
                        create_appbar(root),
                        Container(
                            content=Column(
                                [
                                    Image(src="img/icon.png", width=150, height=150, fit=ImageFit.CONTAIN),
                                    Text("مرحبًا بك في الأسن", size=28, weight=FontWeight.BOLD, color=colors.BLUE_700),
                                    TextField(
                                        label='اسم الطالب',
                                        prefix_icon=icons.PERSON,
                                        border_radius=10,
                                        bgcolor=colors.WHITE,
                                        width=300,
                                        text_align=TextAlign.CENTER
                                    ),
                                    TextField(
                                        label='كود الطلاب',
                                        prefix_icon=icons.LOCK,
                                        password=True,
                                        can_reveal_password=True,
                                        border_radius=10,
                                        bgcolor=colors.WHITE,
                                        width=300,
                                        text_align=TextAlign.CENTER
                                    ),
                                    ElevatedButton(
                                        "تسجيل الدخول",
                                        on_click=lambda _: root.go("/الصفحه الراسية"),
                                        width=200,
                                        height=50,
                                        style=ButtonStyle(
                                            bgcolor=colors.BLUE_700,
                                            color=colors.WHITE,
                                            shape=RoundedRectangleBorder(radius=10),
                                            elevation=5
                                        )
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=20,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )

       
        elif root.route == "/الصفحه الراسية":
            root.views.append(
                View(
                    "/الصفحه الراسية",
                    [
                        create_appbar(root),
                        Container(
                            content=Column(
                                [
                                    Text('جدول المحاضرات', size=30, weight=FontWeight.BOLD, color=colors.BLUE_900),
                                    Card(
                                        content=Container(
                                            Image(src="img/po.jpg", width=340, fit=ImageFit.COVER),
                                            padding=5
                                        ),
                                        elevation=8,
                                        margin=10,
                                        shape=RoundedRectangleBorder(radius=15)
                                    ),
                                    ElevatedButton(
                                        "عرض النتيجة",
                                        on_click=lambda _: root.go("/النتيجه"),
                                        width=200,
                                        height=50,
                                        style=ButtonStyle(
                                            bgcolor=colors.BLUE_700,
                                            color=colors.WHITE,
                                            shape=RoundedRectangleBorder(radius=10),
                                            elevation=5
                                        )
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=20,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER
                )
            )

        
        elif root.route == "/النتيجه":
            root.views.append(
                View(
                    "/النتيجه",
                    [
                        create_appbar(root),
                        Container(
                            content=Column(
                                [
                                    Text("أدخل رقم الجلوس", size=25, weight=FontWeight.BOLD, color=colors.BLUE_900),
                                    TextField(
                                        label='رقم الجلوس',
                                        prefix_icon=icons.NUMBERS,
                                        border_radius=10,
                                        bgcolor=colors.WHITE,
                                        width=300,
                                        text_align=TextAlign.CENTER,
                                        keyboard_type=KeyboardType.NUMBER
                                    ),
                                    ElevatedButton(
                                        "عرض النتيجة",
                                        on_click=lambda _: root.go("/عرض النتيجة"),
                                        width=200,
                                        height=50,
                                        style=ButtonStyle(
                                            bgcolor=colors.BLUE_700,
                                            color=colors.WHITE,
                                            shape=RoundedRectangleBorder(radius=10),
                                            elevation=5
                                        )
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=20,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER
                )
            )

       
        elif root.route == "/المساعدة":
            root.views.append(
                View(
                    "/المساعدة",
                    [
                        create_appbar(root),
                        Container(
                            content=Column(
                                [
                                    Text("مركز المساعدة", size=25, weight=FontWeight.BOLD, color=colors.BLUE_900),
                                    Card(
                                        content=Container(
                                            Image(src='img/po.jpg', width=340, fit=ImageFit.COVER),
                                            padding=5
                                        ),
                                        elevation=8,
                                        margin=10,
                                        shape=RoundedRectangleBorder(radius=15)
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            padding=20,
                            expand=True
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER
                )
            )

        
        elif root.route == "/الشات":
            # حقل إدخال الرسالة
            message_input = TextField(
                label="اكتب رسالتك",
                border_radius=10,
                bgcolor=colors.WHITE,
                width=300,
                multiline=True,
                max_lines=3
            )
            
           
            def send_message(e):
                if message_input.value.strip():  # التأكد من أن الحقل ليس فارغًا
                    timestamp = datetime.now().strftime("%H:%M")  # طابع زمني
                    chat_messages.append({"user": "أنا", "message": message_input.value, "time": timestamp})
                    message_input.value = ""  # تفريغ الحقل
                    update_chat()

         
            def update_chat():
                chat_container.content.controls = [
                    Card(
                        content=Container(
                            Column([
                                Row([Text(f"{msg['user']}", weight=FontWeight.BOLD), Text(f"{msg['time']}", size=12, color=colors.GREY_600)], alignment=MainAxisAlignment.SPACE_BETWEEN),
                                Text(msg["message"])
                            ]),
                            padding=10
                        ),
                        elevation=2,
                        shape=RoundedRectangleBorder(radius=10),
                        margin=5
                    ) for msg in chat_messages
                ]
                root.update()

            # حاوية الرسائل مع التمرير
            chat_container = Container(
                content=Column([], scroll="auto", height=400),
                expand=True
            )
            
            update_chat()

            root.views.append(
                View(
                    "/الشات",
                    [
                        create_appbar(root),
                        Container(
                            content=Column(
                                [
                                    Text("غرفة الشات", size=25, weight=FontWeight.BOLD, color=colors.BLUE_900),
                                    chat_container,  # عرض الرسائل
                                    Row([
                                        message_input,
                                        IconButton(
                                            icon=icons.SEND,
                                            bgcolor=colors.BLUE_700,
                                            icon_color=colors.WHITE,
                                            on_click=send_message
                                        )
                                    ], alignment=MainAxisAlignment.CENTER)
                                ],
                                spacing=10,
                                expand=True
                            ),
                            padding=20
                        )
                    ]
                )
            )

        
        else:
            root.views.append(
                View(
                    root.route,
                    [
                        create_appbar(root),
                        Container(
                            content=Text("الصفحة غير موجودة", size=20, color=colors.RED),
                            alignment=alignment.center,
                            expand=True
                        )
                    ]
                )
            )
        
        root.update()

   
    def root_go(view):
        if len(root.views) > 1:
            root.views.pop()
            back_page = root.views[-1]
            root.go(back_page.route)

    
    root.on_route_change = route_change
    root.on_view_pop = root_go
    root.go(root.route)


app(target=main, assets_dir='assets')
