import flet as ft
import random, os
import ns


grid_width, grid_height = 24, 12
cell_size = 40

on = "#ffffff"
off = "#8fabdd"

def main(page: ft.Page):
    page.title = "DTEK casino"
    page.fonts = {
        "e-Ukraine": "fonts/e-Ukraine-Regular.otf",
        "PollyRounded-Bold": "fonts/PollyRounded-Bold.ttf"
    }
    page.theme = ft.Theme(font_family = "e-Ukraine")
    page.theme_mode = ft.ThemeMode.DARK

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    line1_cells = []
    line2_cells = []
    line3_cells = []
    line_time_cells = []
    lines = []

    for i in range(6):
        line1_cells.append(
            ft.Container(
                width = cell_size,
                height = cell_size*2+1,
                content = ft.Text(value=i+1, color=ft.Colors.BLACK),
                bgcolor = on,
                alignment = ft.alignment.center,
                expand = True
            )
        )

    for i in range(6):
        line2_cells.append(
            ft.Container(
                width = cell_size,
                height = cell_size,
                bgcolor = on,
                alignment = ft.alignment.center,
                content = ft.Text(value=f"{i+1}.1", color=ft.Colors.BLACK),
                expand = True
            )
        )
        line2_cells.append(
            ft.Container(
                width = cell_size,
                height = cell_size,
                bgcolor = on,
                alignment = ft.alignment.center,
                content = ft.Text(value=f"{i+1}.2", color=ft.Colors.BLACK),
                expand = True
            )
        )

    for y in range(grid_height):
        row_cells = []
        for x in range(grid_width):
            cell = ft.Container(
                width = cell_size,
                height = cell_size,
                bgcolor = random.choice([on, off]),
            )
            row_cells.append(cell)
        line = ft.Row(controls=row_cells, spacing=1)
        lines.append(line)

    for i in range(grid_height):
        blue_cells = sum(1 for cell in lines[i].controls if cell.bgcolor == off)
        line3_cells.append(
            ft.Container(
                width = cell_size*3+2,
                height = cell_size,
                bgcolor = on,
                alignment = ft.alignment.center,
                content = ft.Text(value=str(blue_cells), color=ft.Colors.BLACK),
                expand = True
            )
        )
    
    for i in range(grid_width):
        start_hour = i
        end_hour = (i + 1) % 24
        time_text = f"{start_hour:02d}:\n00\n-\n{end_hour:02d}:\n00"

        line_time_cells.append(
            ft.Container(
                width = cell_size,
                height = cell_size*3+2,
                bgcolor = on,
                alignment = ft.alignment.center,
                content = ft.Text(
                    value = time_text,
                    color = ft.Colors.BLACK,
                    text_align = ft.TextAlign.CENTER
                ),
                expand = True
            )
        )

    line_times = ft.Row(
        controls = line_time_cells,
        spacing = 1,
        alignment = ft.MainAxisAlignment.START
    )

    line_1 = ft.Column(
        controls = line1_cells,
        spacing = 1,
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    line_2 = ft.Column(
        controls = line2_cells,
        spacing = 1,
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )
    
    grid = ft.Column(
        controls = lines,
        spacing = 1,
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    line_3 = ft.Column(
        controls = line3_cells,
        spacing = 1,
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    page.add(
        ft.Container(
            content = ft.Column(
                controls = [
                    ft.Row(
                        controls = [
                            ft.Container(
                                content = ft.Text(
                                    value = "Черга/підчерга",
                                    color = ft.Colors.BLACK,
                                    text_align = ft.TextAlign.CENTER
                                ),
                                width = cell_size*2+1,
                                height = cell_size*3+2,
                                bgcolor = on,
                                alignment = ft.alignment.center
                            ),
                            line_times,
                            ft.Container(
                                content = ft.Text(
                                    value = "Фактична тривалість відключень за добуб год",
                                    color = ft.Colors.BLACK,
                                    text_align = ft.TextAlign.CENTER
                                ),
                                width = cell_size*3+2,
                                height = cell_size*3+2,
                                bgcolor = on,
                                alignment = ft.alignment.center
                            )
                        ],
                        spacing = 1,
                        alignment = ft.MainAxisAlignment.START
                    ),
                    ft.Row(
                        controls = [
                            line_1,
                            line_2,
                            grid,
                            line_3
                        ],
                        spacing = 1,
                        alignment = ft.MainAxisAlignment.START
                    )
                ],
                spacing = 1,
                alignment = ft.MainAxisAlignment.START
            )
        )
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2496))
    ft.app(target = main, view = ft.WEB_BROWSER, port = port)