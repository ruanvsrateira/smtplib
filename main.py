import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Seu E-mail
email_remetente = "example@gmail.com"
# Senha E-mail
email_senha = "example"
# Email Destino
email_destino = "example@gmail.com"
# Titulo do E-mail
email_titulo = "example"
# Corpo do E-mail
email_corpo = "example"

# Configurando Servidor de E-mail
servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
servidor_email.starttls()
servidor_email.login(email_remetente, email_senha)

# Criando mensagem
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = email_destino
msg['Subject'] = email_titulo
msg.attach(MIMEText(email_corpo, 'plain'))

# Enviando E-mail
servidor_email.sendmail(email_remetente, email_destino, msg.as_string())

