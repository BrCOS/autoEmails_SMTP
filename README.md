# autoEmails_SMTP
Script que envia e-mails de forma automática via SMTP, pré configurado para Gmail e Outlook e também permitindo que seja configurado um SMTP personalizado.

# autoEmail

Envia e-mails de forma automática para qualquer provedor de e-mail, pré configurado para gmail e outlook.
Defina a data e hora e ao chegar a data, sua mensagem será enviada para o destinatário.


# GMAIL

Para poder enviar e-mails de um e-mail **@gmail.com**, vá até a sua conta google e clique em **Gerenciar sua Conta do Google**, ou digite https://myaccount.google.com/.

No **Menu Lateral à Esquerda**, vá até a opção de **Segurança** e no menu **Como você faz login no Google** vá até a opção **Verificação em duas etapas**, se não estiver habilitada, faça login e habilite esta opção, caso já esteja habilitada, faça login e vá até a opção de **Senhas de app**.

Dentro da opção Senhas de app, na opção de **Selecionar app** procure por **Outro (nome personalizado)**, digite o nome que quiser e clique em **Gerar**. No pop-up que aparecer, aparecerá uma senha destacada, esta senha será a senha que você irá digitar para enviar e-mails via SMTP no script.

Desta forma, não será necessário informar a sua senha Google (senha do Gmail) para poder enviar e-mails via SMTP, apenas a senha gerada e que pode ser revogada a qualquer momento, seguindo os mesmos passos acima.

> Até 2022, o Google permitia o acesso a apps menos seguros, porém essa opção foi removida devido ás políticas de segurança Google.

## Outlook | Hotmail

Diferente do Gmail, para enviar e-mails via SMTP com o provedor da microsoft, será necessário informar a sua senha do Outlook e **autorizar o script em 'Atividades da Conta'.**

Digite https://account.microsoft.com/activity para poder acessar e autorizar o script, por favor, verifique as informações antes de autorizar, tais como 'protocolo' que deve ser 'SMTP', hora (que deve ser correspondente a hora em que o script foi executado) e também o tipo que deve ser 'Sincronização bem-sucedida', pois verifica se os dados informados da conta estão corretos.

## Outros Provedores

Será necessário verificar com o seu provedor o endereço do SMTP, porta e também o tipo de conexão (SSL ou Starttls).

## Verificação de Data e Hora

O script verifica a cada 5 segundos se a data e hora atual é a data e hora de enviar o e-mail (baseada na data e hora definida pelo usuário).

O Script deve ficar aberto para poder enviar o e-mail na data e hora desejada.
