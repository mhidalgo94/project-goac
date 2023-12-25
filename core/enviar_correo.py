import smtplib
import socks


#'PROXY_TYPE_SOCKS4' puedes replazarlo por HTTP o PROXY_TYPE_SOCKS5
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, '10.1.107.19', 3128, 'email', 'password') # usuario y pass del proxy
socks.wrapmodule(smtplib)

smtpserver = 'smtp.gmail.com'
smtpuser = 'marito.hidalgo94@gmail.com'
smtppass = 'gmailhr9420*'

print('Conectando')
server = smtplib.SMTP(smtpserver,587)
print(server.ehlo())
server.starttls()
print(server.ehlo())
server.login(smtpuser,smtppass)


# def enviar_correo():
#     try:
#         print('Conectando')
#         mailServer = smtplib.SMTP('smtp.gmail.com',587)
#         print(mailServer.ehlo())
#         mailServer.starttls()
#         print(mailServer.ehlo())
#         mailServer.login('correo@gmail.com','password')
#         print('Conexion establecida')
#     except Exception as e:
#         print(e)

# enviar_correo()
