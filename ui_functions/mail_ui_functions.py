from mail_content.html_template import html_template


signature_urls = {
    "Liam": "https://i.imgur.com/uKpk39B.png",
    "Tof": "https://i.imgur.com/Lbkp32T.png",
    "Lucas": "https://i.imgur.com/Qip3drn.png",
    "Boris": "https://i.imgur.com/rPpdfk3.png"
}

def update_preview_mail(receivers_dropdown,title_input,content_greetings_input,content_input,content_question_input,signature_input,picture_input,button_text_input,button_link_input,web_view):
    receiver = receivers_dropdown.currentText()
    title = title_input.text()
    content_greetings = content_greetings_input.toPlainText()
    content = content_input.toPlainText()
    content_question = content_question_input.toPlainText()
    selected_signature = signature_input.currentText()
    if selected_signature in signature_urls:
        image_url = signature_urls[selected_signature]
    
    picture = picture_input.text()
    button_text = button_text_input.text()
    button_link = button_link_input.text()

    html_content = html_template.format(
        title=title,
        body_bg_color="#ffffff",
        text_color="#000000",
        font_family="Della Respira, serif",
        font_size=20,
        image_src=picture,
        text_greeting=f"Bonjour <<PRENOM>>, <br><br>{content_greetings}",
        text_content=f"<br><br>{content}",
        text_question=f"<br><br>{content_question}",
        text_signature=f"<br><br>Cordialement, <br> <br><img src='{image_url}'/>",
        button_link=button_link,
        button_text=button_text,
        button_text_color="#edead5",
        button_bg_color="#000000",
        button_font_size=20,
    )
    web_view.setHtml(html_content)
    return html_content