# 🛠 Port Scanner em Python

## 📌 Descrição
Este projeto é um **scanner de portas TCP** desenvolvido em Python com foco didático.  
Permite verificar quais portas estão abertas em um **host** (IP ou nome) dentro de um intervalo definido.

### Recursos:
- Varredura **sequencial** (didática).
- Suporte a **hostname ou IP**.
- Configuração de **intervalo de portas**.
- **Timeout** ajustável.
- **Relatório opcional** em **JSON**, **CSV** ou **Markdown**.

---

## ✅ Pré-requisitos
- Python **3.8+** instalado.
- Executar via **linha de comando (CLI)**.

---

## 📥 Instalação
Clone o repositório ou copie o arquivo `port_scanner.py` para sua máquina.

```bash
git clone https://github.com/seuusuario/port-scanner.git
cd port-scanner
```

---

## ▶️ Como usar

### **Comando básico**
```bash
python port_scanner.py --host scanme.nmap.org
```
> Faz um scan no host `scanme.nmap.org` nas portas **1 a 1024** com timeout padrão (0.5s).

---

### **Definir intervalo de portas**
```bash
python port_scanner.py --host scanme.nmap.org --start 20 --end 90
```
> Varre da porta **20 até a 90**.

---

### **Definir timeout**
```bash
python port_scanner.py --host scanme.nmap.org --timeout 1
```
> Cada tentativa espera **1 segundo** antes de desistir.

---

### **Gerar relatório**
Você pode salvar os resultados em **JSON**, **CSV** ou **Markdown**:

#### JSON:
```bash
python port_scanner.py --host scanme.nmap.org --format json --out relatorio.json
```

#### CSV:
```bash
python port_scanner.py --host scanme.nmap.org --format csv --out relatorio.csv
```

#### Markdown:
```bash
python port_scanner.py --host scanme.nmap.org --format md --out relatorio.md
```

---

## 📂 Onde o arquivo será salvo?
- Se você usar `--out relatorio.json`, o arquivo será salvo **no diretório atual**.
- Para salvar em outro local, informe o caminho completo:
```bash
python port_scanner.py --host scanme.nmap.org --format json --out "C:\Users\Thiago\Desktop\scan.json"
```

---

## ⚠️ Aviso legal
Use este scanner **apenas em hosts autorizados**.  
Exemplo seguro: `scanme.nmap.org` (fornecido pelo Nmap para testes educacionais).

---

## 🔮 Próximos passos (cronograma)
- **Semana 2**: saída estruturada (JSON/CSV/MD), barra de progresso.
- **Semana 3**: suporte IPv6, mapeamento de serviços.
- **Semana 4**: versão concorrente com `asyncio` para alta performance.
