#color set

def colors(appearance_mode):
        global main_accent_color,secondary_accent_color,unselected_color,main_color,frame_color,text_color
        
        D_main_accent_color="#1f6aa4"
        D_secondary_accent_color = "#154870"
        D_unselected_color= "#4a4d4f"
        D_main_color="#212325"
        D_frame_color="#2b2b2b"
        D_text_color="#d5d9de"

        L_main_accent_color="#3b8ed0"
        L_secondary_accent_color = "#36719f"
        L_unselected_color ="#939ba2"
        L_main_color="#ebebeb"
        L_frame_color="#dbdbdb"
        L_text_color="#1b1b1b"

        if appearance_mode == 'Dark':
            colors.main_accent_color=D_main_accent_color
            colors.secondary_accent_color=D_secondary_accent_color
            colors.unselected_color=D_unselected_color
            colors.main_color=D_main_color
            colors.frame_color=D_frame_color
            colors.text_color=D_text_color

        elif appearance_mode == 'Light':
            colors.main_accent_color=L_main_accent_color
            colors.secondary_accent_color=L_secondary_accent_color
            colors.unselected_color=L_unselected_color
            colors.main_color=L_main_color
            colors.frame_color=L_frame_color
            colors.text_color=L_text_color