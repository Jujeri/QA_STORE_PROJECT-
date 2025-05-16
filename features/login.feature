Feature: Login de usuário

  Scenario: Login com credenciais válidas
    Given que o usuário está na página de login
    When ele preenche o usuário "admin" e senha "admin123"
    And clica no botão de login
    Then ele deve ver a página inicial

