html_template = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="x-apple-disable-message-reformatting">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{title}</title>
</head>
<body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: {body_bg_color};color: {text_color}; font-family: {font_family}">
<table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: {body_bg_color};width:100%" cellpadding="0" cellspacing="0">
  <tbody>
    <tr style="vertical-align: top">
      <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <div class="u-row-container" style="padding: 0px;background-color: transparent">
          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 740px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
              <div class="u-col u-col-100" style="max-width: 320px;min-width: 740px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                  <table style="font-family:'{font_family}';" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                    <tbody>
                      <tr>
                        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'{font_family}';" align="left">
                          <table width="100%" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td style="padding-right: 0px;padding-left: 0px;" align="center">
                                <img align="center" border="0" src="{image_src}" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 512px;" width="512"/>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <table style="font-family:'Della Respira',serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                    <tbody>
                      <tr>
                        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:30px 50px;font-family:'{font_family}';" align="left">
                          <div style="font-size: {font_size}px; line-height: 180%; text-align: center; word-wrap: break-word;">
                            <p style="line-height: 180%;">{text_greeting}{text_content}{text_question}</p>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div align="center">
                    <a href="{button_link}" target="_blank" class="v-button v-size-width" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: {button_text_color}; background-color: {button_bg_color}; border-radius: 30px;-webkit-border-radius: 30px; -moz-border-radius: 30px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;border-top-width: 0px; border-top-style: solid; border-left-width: 0px; border-left-style: solid; border-right-width: 0px; border-right-style: solid; border-bottom-width: 0px; border-bottom-style: solid;font-size: {button_font_size}px;">
                      <span style="display:block;padding:15px 40px;line-height:180%;">{button_text}</span>
                    </a>
                    <div style="font-size: {font_size}px; line-height: 180%; text-align: center; word-wrap: break-word;">
                    <p style="line-height: 180%;">{text_signature}</p>
                    <div>
                  </div>
                      <table id="u_body" style="border-collapse: collapse; table-layout: fixed; border-spacing: 0; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; min-width: 320px; margin: 0 auto; background-color: #ffffff; width: 100%;" cellpadding="0" cellspacing="0">
                      <tbody>
                          <!-- ... (other table rows and cells here) ... -->
                          <tr>
                            <td class="v-container-padding-padding" style="overflow-wrap: break-word; word-break: break-word; padding: 10px; font-family: {font_family};" align="left">
                                <!-- ... (content within the table cell) ... -->
                                <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; table-layout: fixed; border-spacing: 0; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; border-top: 5px solid #000000; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                    <tbody>
                                        <tr style="vertical-align: top">
                                            <td style="word-break: break-word; border-collapse: collapse !important; vertical-align: top; font-size: 0px; line-height: 0px; mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                <span>&#160;</span>
                              </td>
                          </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>
</body>
</html>
"""