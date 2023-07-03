# autoEmails_SMTP
Script que envia e-mails de forma automática via SMTP, pré configurado para Gmail e Outlook e também permitindo que seja configurado um SMTP personalizado.

# autoEmail

Envia e-mails automaticamente para qualquer provedor de e-mail, pré-configurado para Gmail e Outlook.
Defina a data e hora, e quando essa data chegar, sua mensagem será enviada para o destinatário.

# GMAIL

Para enviar e-mails de um endereço **@gmail.com**, vá até sua conta Google e clique em **Gerenciar sua Conta do Google**, ou acesse https://myaccount.google.com/.

No **Menu Lateral Esquerdo**, vá até a opção de **Segurança** e, no menu **Como você faz login no Google**, vá até a opção **Verificação em duas etapas**. Se não estiver habilitada, faça login e habilite essa opção. Se já estiver habilitada, faça login e vá até a opção **Senhas de app**.

Dentro da opção Senhas de app, em **Selecionar app**, procure por **Outro (nome personalizado)**, digite o nome que preferir e clique em **Gerar**. Em um pop-up, será exibida uma senha destacada. Essa será a senha que você irá digitar para enviar e-mails via SMTP no script.

Dessa forma, não será necessário informar sua senha do Google (senha do Gmail) para enviar e-mails via SMTP, apenas a senha gerada, que pode ser revogada a qualquer momento, seguindo os mesmos passos mencionados.

> A partir de 2022, o Google deixou de permitir o acesso a apps menos seguros devido às políticas de segurança.

## OUTLOOK | HOTMAIL

Diferente do Gmail, para enviar e-mails via SMTP com o provedor da Microsoft, será necessário informar sua senha do Outlook e **autorizar o script nas 'Atividades da Conta'.**

Acesse https://account.microsoft.com/activity para acessar e autorizar o script. Por favor, verifique as informações antes de autorizar, como o 'protocolo', que deve ser 'SMTP', a hora (que deve corresponder ao momento em que o script foi executado) e também o tipo, que deve ser 'Sincronização bem-sucedida' para verificar se os dados da conta informados estão corretos.

## OUTROS PROVEDORES

Será necessário verificar com seu provedor o endereço do servidor SMTP, a porta e também o tipo de conexão (SSL ou Starttls).

## VERIFICAÇÃO DE DATA E HORA

O script verifica a cada 5 segundos se a data e hora atual correspondem à data e hora definidas pelo usuário para enviar o e-mail.

O script deve permanecer aberto para que o e-mail seja enviado na data e hora desejadas.
