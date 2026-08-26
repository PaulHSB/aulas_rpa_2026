# bot_initializer.py

# Declaração e inicialização das variáveis de configuração do robô
BOT_NAME: str = "RPA_FINANCEIRO_01"
MAX_RETRIES: int = 3
EXECUTION_TIMEOUT: float = 30.0
IS_PRODUCTION: bool = False

# Mensagem de inicialização formatada
print("=" * 50)
print("       INICIALIZAÇÃO DO ROBÔ RPA")
print("=" * 50)
print(f"  BOT_NAME          : {BOT_NAME}")
print(f"  Tipo              : {type(BOT_NAME)}")
print(f"  MAX_RETRIES       : {MAX_RETRIES}")
print(f"  Tipo              : {type(MAX_RETRIES)}")
print(f"  EXECUTION_TIMEOUT : {EXECUTION_TIMEOUT}")
print(f"  Tipo              : {type(EXECUTION_TIMEOUT)}")
print(f"  IS_PRODUCTION     : {IS_PRODUCTION}")
print(f"  Tipo              : {type(IS_PRODUCTION)}")
print("=" * 50)
print("  Robô inicializado com sucesso!")
print("=" * 50)
