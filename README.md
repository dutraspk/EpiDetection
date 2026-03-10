# EpiDetection
---
## Projeto
O projeto é baseado em Phyton, e consiste em uma placa (possivelmente SBC) e terá um sistema integrado que irá detectar se a pessoa está fazendo ou não o uso de EPI, e quando ela está usando tudo corretamente, através de uma câmera, o sistema analisa e libera a entrada da pessoa abrindo a porta (neste contexto, aplicado à entrada da fábrica), e se o equipamento está fora da validade, em um visor próximo é mostrado o motivo da não liberação. O sistema também teria um controle de validade dos EPIs, sendo feito por código de barras ou alguma tag. Para a abertura da porta, o sistema utilizaria uma fechadura solenoide ligada ao circuito, fazendo a abertura da porta.
Todos os dados coletados pelos sistemas são entregues à um banco central de dados onde o gerente ou supervisor de segurança ficaria monitorando os dados.

Sobre o interior da fábrica, teria o sistema implementado nas câmeras de segurança e teria o mesmo conceito de detectar o uso ou não uso de EPI, assim, enviando os dados para o banco de dados, mas não é relevante no momento.