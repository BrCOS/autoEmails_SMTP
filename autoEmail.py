import ssl
from email.message import EmailMessage
import smtplib
import datetime
import time


def email():
    emailRemetente = input('Digite o e-mail do remetente: ')
    senhaRemetente = input('Digite a senha do e-mail do remetente: ')
    emailDestinatario = input('Digite o email de destinatário: ')

    assunto = input('Digite o assunto do E-mail: ')
    corpoEmail = input('Digite a mensagem a ser enviada: ')

    dataEnviar = input('Digite a data para enviar o e-mail DD/MM/ANO: ')
    horaEnviar = input('Digite a hora para enviar o e-mail HH:MM: ')

    dia, mes, ano = map(int, dataEnviar.split('/'))
    hora, minutos = map(int, horaEnviar.split(':'))

    if ano < 100:
        ano += 2000

    dataHoraEnviar = datetime.datetime(ano, mes, dia, hora, minutos)  #padrao americano

    email = EmailMessage()
    email['From'] = emailRemetente
    email['To'] = emailDestinatario
    email['Subject'] = assunto
    email.set_content(corpoEmail)

    emailProvedor = emailRemetente.split('@')[1]

    if emailProvedor == 'gmail.com':
        context = ssl.create_default_context()
        while True:
            dataHoraAgora = datetime.datetime.now()
            if dataHoraAgora >= dataHoraEnviar:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(emailRemetente, senhaRemetente)
                    smtp.sendmail(emailRemetente, emailDestinatario, email.as_string())
                    smtp.quit()
                print(f'E-mail enviado com sucesso para o Destinatário: {emailDestinatario}')
                break
            else:
                print('Ainda não está na hora.')
                print(dataHoraAgora)
                time.sleep(5)
                
    elif emailProvedor == 'outlook.com' or emailProvedor == 'outlook.com.br' or emailProvedor == 'hotmail.com':
        while True:
            dataHoraAgora = datetime.datetime.now()
            if dataHoraAgora >= dataHoraEnviar:
                with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                    smtp.starttls()
                    smtp.login(emailRemetente, senhaRemetente)
                    smtp.sendmail(emailRemetente, emailDestinatario, email.as_string())
                    smtp.quit()
                print(f'E-mail enviado com sucesso para o Destinatário: {emailDestinatario}')
                break
            else:
                print('Ainda não está na hora.')
                print(dataHoraAgora)
                time.sleep(5)

    else:
        outroProvedor = input('Provedor de E-mail não suportado.\nDeseja configurar um provedor? - Digite S ou N: ').upper()
        if outroProvedor == 'S':
            provedorSmtp = input('Digite o Servidor SMTP: ')
            portaSmtp = int(input('Digite a porta do Servidor SMTP: '))
            tipoConexao = input('A conexão é SSL ou Starttls? ').upper()
            if tipoConexao == 'SSL':
                while True:
                    dataHoraAgora = datetime.datetime.now()
                    if dataHoraAgora >= dataHoraEnviar:
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL(provedorSmtp, portaSmtp, context=context) as smtp:
                            smtp.login(emailRemetente, senhaRemetente)
                            smtp.sendmail(emailRemetente, emailDestinatario, email.as_string())
                            smtp.quit()
                        print(f'E-mail enviado com sucesso para o Destinatário: {emailDestinatario}')
                        break
                    else:
                        print('Ainda não está na hora.')
                        print(dataHoraAgora)
                        time.sleep(5)

            elif tipoConexao == 'STARTTLS':
                while True:
                    dataHoraAgora = datetime.datetime.now()
                    if dataHoraAgora >= dataHoraEnviar:
                        with smtplib.SMTP(provedorSmtp, portaSmtp) as smtp:
                            smtp.starttls()
                            smtp.login(emailRemetente, senhaRemetente)
                            smtp.sendmail(emailRemetente, emailDestinatario, email.as_string())
                            smtp.quit()
                        print(f'E-mail enviado com sucesso para o Destinatário: {emailDestinatario}')
                        break
                    else:
                        print('Ainda não está na hora.')
                        print(dataHoraAgora)
                        time.sleep(5)

            else:
                print('Digite SSL ou Starttls!')

        else:
            print('Configuração Encerrada!')


email()