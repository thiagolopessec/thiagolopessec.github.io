"""
Projeto: Port Scanner em Python
Autor: Thiago Lopes
Descrição:
Scanner de portas TCP com suporte a:
- Alvo por IP ou hostname
- Range de portas
- Timeout configurável
- Execução sequencial (baseline didático)

Uso:
python port_scanner.py --host scanme.nmap.org --start 1 --end 1024
"""

import socket
import argparse
from datetime import datetime, timedelta


def scan_port(host: str, port: int, timeout: float) -> bool:
    """Tenta conexão TCP em uma porta específica (IPv4).

    Retorna True se a porta aceitar conexão TCP (connect_ex == 0).
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except (socket.gaierror, socket.timeout, socket.error):
        return False


def run_scan(host: str, start_port: int, end_port: int, timeout: float):
    # Validações de entrada
    if start_port < 1 or end_port > 65535:
        raise ValueError("O intervalo de portas deve estar entre 1 e 65535")
    if start_port > end_port:
        raise ValueError("Porta inicial não pode ser maior que a final")
    if timeout <= 0:
        raise ValueError("Timeout deve ser maior que 0")

    # Resolve hostname para IPv4
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror as e:
        raise ValueError(f"Host inválido '{host}': {e}")

    open_ports = []

    inicio = datetime.now()
    print(f"[*] Iniciando scan em {host} ({target_ip})")
    print(f"[*] Portas: {start_port}-{end_port}")
    print(f"[*] Início: {inicio}")

    try:
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port, timeout):
                print(f"[+] Porta aberta: {port}")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\n[!] Interrompido pelo usuário. Saindo...")

    fim = datetime.now()
    duracao = fim - inicio
    if isinstance(duracao, timedelta):
        duracao_str = str(duracao).split(".")[0]
    else:
        duracao_str = str(duracao)

    print("\n[*] Scan finalizado")
    print(f"[*] Fim: {fim}")
    print(f"[*] Duração: {duracao_str}")

    if open_ports:
        print("[+] Portas abertas encontradas:")
        for p in open_ports:
            print(f"    - {p}")
    else:
        print("[-] Nenhuma porta aberta encontrada")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner TCP em Python")
    parser.add_argument("--host", required=True, help="IP ou hostname do alvo")
    parser.add_argument("--start", type=int, default=1, help="Porta inicial")
    parser.add_argument("--end", type=int, default=1024, help="Porta final")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout em segundos")
    args = parser.parse_args()
    try:
        run_scan(args.host, args.start, args.end, args.timeout)
    except ValueError as e:
        print(f"[!] Erro: {e}")
        exit(1)
