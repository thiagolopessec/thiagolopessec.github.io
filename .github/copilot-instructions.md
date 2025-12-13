# Instruções do Copilot para thiagolopessec.github.io

<<<<<<< HEAD
**Objetivo**: orientar agentes de IA a trabalharem de forma produtiva neste site de portfólio Blue Team. Mantenha mudanças consistentes com o design de segurança, focadas em conteúdo bilíngue, acessibilidade e desempenho.

## Arquitetura

**Site estático com dois endpoints principais**:
- [index.html](index.html) – Página principal: **Blue Team Security Portfolio** (design moderno em CSS-in-HTML com tema de segurança)
- [thiagolopessec.github.io/index.html](thiagolopessec.github.io/index.html) – **Página alternativa** com design legacy (será descontinuada ou sincronizada)
- [dicionario.html](thiagolopessec.github.io/dicionario.html) – **Dicionário Python interativo** com busca em tempo real
- Sem frameworks/bundlers. Sem gerenciador de pacotes. Vanilla HTML/CSS/JavaScript.

**Assets compartilhados** (em `thiagolopessec.github.io/assets/`):
- [style.css](thiagolopessec.github.io/assets/css/style.css) – Tema legacy (ainda em uso para dicionário)
- [main.js](thiagolopessec.github.io/assets/js/main.js) – i18n centralizado com `data-translate` e language switcher
- [data.js](thiagolopessec.github.io/assets/js/data.js) – Dados do dicionário (tipos_python, pitfalls, exemplos bilíngues)
- [dicionario.js](thiagolopessec.github.io/assets/js/dicionario.js) – Busca interativa

## Padrão Principal: index.html (Blue Team Security Portfolio)

### CSS Variables (Segurança / Dashboard)
```css
:root {
  --bg-body: #0a0a0b;
  --bg-card: #121214;
  --bg-card-hover: #1c1c1f;
  --text-primary: #ededed;
  --text-secondary: #a1a1aa;
  --accent-primary: #10b981; /* Emerald Green */
  --accent-secondary: #3b82f6; /* Blue */
  --accent-purple: #8b5cf6; /* LGPD/Governance */
  --accent-alert: #ef4444; /* Red */
}
```

### Estrutura HTML
- Semântica: `<header>`, `<section>`, `<footer>` obrigatórios
- **Sem classes CSS** – tudo em `<style>` inline (arquivo único, sem deps)
- `data-translate="chave"` para i18n dinâmica
- Seletor de idioma: `.lang-switch` com botões `.lang-btn` (PT/EN)
- `.reveal` para animações de entrada (Intersection Observer)

### Seções Padrão
1. **Header** – Profile container com status ring animado, bio, social links
2. **Education & Certs** – Timeline visual com status (done/active/future)
3. **Tech Stack** – Cartões `.card` com ícones e tags
4. **Projects** – Cards com border-left colorida (primary/secondary)
5. **Roadmap (Timeline)** – 4 fases com markers animados
6. **Lab** – Terminal interativo com cipher Caesar (encrypt/decrypt)

## Sistema de Tradução (i18n)

### Estrutura em main.js
```javascript
const translations = {
  pt: { bio: "...", edu_title: "01. Formação & Certificações", ... },
  en: { bio: "...", edu_title: "01. Education & Certs", ... }
};
```

### Aplicação no HTML
- Use `data-translate="chave"` em elementos
- Função `app.setLang(lang)` atualiza `.innerHTML` via `translations[lang]`
- Persistence via `localStorage.getItem('lang')`

**Regra crítica**: toda adição de texto = entrada em **ambas** pt e en.

## Padrões de Código

### JavaScript no index.html
- Strict mode: `"use strict"` (comentário na primeira linha)
- IIFE: `(function(){...})()`
- Sem deps externas
- Métodos em `const app = { lang, setLang(), encrypt(), decrypt(), ... }`
- Events com `addEventListener`, `onclick` apenas para botões simples
- Acessibilidade: `aria-label`, `role="main"`, `role="region"`

### CSS no index.html
- **Tudo em `<style>` inline** – ordem: resets, vars, body, header, sections, cards, timeline, terminal, reveal, media
- Transitions: `0.2s`, `0.3s` ease
- Animations: `spin` (rotating status ring), `pulse` (timeline marker)
- Mobile-first: `@media (max-width: 640px)` para ajustes de fonte

### Animações de Entrada
- `.reveal` classe com `opacity: 0; transform: translateY(20px)`
- Intersection Observer dispara `.reveal.active` quando 10% visível
- Respeitoso a `prefers-reduced-motion`

### Dicionário (legacy em data.js / dicionario.js)
- Dados: `window.tipos_python = { term: "code", ... }`
- Pitfalls: `window.pitfalls` (PT), `window.pitfalls_en` (EN)
- Exemplos: `window.exemplos` (PT), `window.exemplos_en` (EN)
- Busca: lowercased, matches termo/código/pitfall/exemplo
- Renderização: `.result-card` com `.pitfall` e `.example` como `<pre>`

## Fluxos de Trabalho

**Prévia local**:
```powershell
python -m http.server 8080
# Acesse http://localhost:8080 (raiz = index.html novo)
# Acesse http://localhost:8080/thiagolopessec.github.io/dicionario.html
```

**Implantação**: GitHub Pages (branch `main`, raiz repo). Caminhos relativos automáticos.

**Sem build/CI/CD** – edite HTML/CSS/JS diretamente.

## Tarefas Comuns

- **Atualizar seção**: edite `<section>` no [index.html](index.html), atualize `translations` correspondente
- **Adicionar card skill/projeto**: duplique `.card`, ajuste ícone/cores via CSS vars
- **Nova timeline item**: duplique `.timeline-item`, altere data/status (done/active/future)
- **Adicionar termo dicionário**: edite [data.js](thiagolopessec.github.io/assets/js/data.js) com PT + EN
- **Alterar tema**: mude `:root` vars no `<style>`

## Pontos Críticos

- **Bilíngue obrigatório**: todo texto visível = PT + EN em `translations`
- **CSS em estilo inline**: não crie arquivos CSS separados sem aprovação
- **Sem frameworks**: nada de React/Vue/Svelte/Tailwind
- **Acessibilidade**: `alt` em imagens, `aria-label` em elementos funcionais, semântica HTML
- **Console easter egg**: `window.showMyStory()` existe (função story em console)
- **Mobile**: teste com redimensionamento (640px breakpoint)
=======
Objetivo: orientar agentes de IA a trabalharem de forma produtiva neste site de portfólio estático. Mantenha mudanças mínimas, consistentes com o estilo atual, focadas em conteúdo, acessibilidade, desempenho e implantação.

## Arquitetura
- **Site estático**: ponto único em [index.html](index.html) com recursos em [assets/](assets).
- **Estilos**: folha central em [assets/css/style.css](assets/css/style.css); variáveis em `:root` definem cores e design.
- **Scripts**: melhorias leves em [assets/js/main.js](assets/js/main.js) (rolagem suave em âncoras). Sem frameworks/bundlers.
- **Imagens**: referenciadas por caminhos relativos (ex.: [assets/img/profile.jpg](assets/img/profile.jpg), [assets/img/banner.jpeg](assets/img/banner.jpeg)). Preserve caminhos ao adicionar conteúdo.

## Convenções e Padrões
- **Idioma**: conteúdo em Português do Brasil. Preserve tom e idioma.
- **Tokens de design**: use variáveis CSS `--primary`, `--secondary`, `--text`, `--bg`, `--card-bg`; evite cores fixas.
- **Layout**: seções usam `.section` e `.alt`; cartões seguem `.skill-card` e `.project-card`; botões `.btn` e `.btn-alt`.
- **Links**: âncoras internas `href="#..."` rolam suavemente; links externos com `target="_blank"` devem incluir `rel="noopener noreferrer"` ao editar.
- **Imagens**: sempre defina `alt`; mantenha proporção e tamanhos do `.profile-photo` e banner.
- **Acessibilidade**: mantenha tags semânticas (`header`, `section`, `footer`) e hierarquia clara (`h1` → `h2`); garanta contraste pelas variáveis.

## Fluxos de Trabalho
- **Prévia local**: abra [index.html](index.html) ou sirva com servidor simples para evitar CORS. Exemplo PowerShell:
  ```powershell
  # Opção 1: Python
  python -m http.server 8080
  # Opção 2: Node (se disponível)
  npx serve . -l 8080
  ```
- **Implantação**: GitHub Pages a partir da branch `main` com raiz do repositório. Mantenha caminhos relativos e evite etapas de build.
- **Sem build/testes**: não há gerenciador de pacotes ou testes. Não introduza tooling sem solicitação.

## Pontos de Integração
- **Fontes externas**: Google Fonts via `@import` no CSS. Para performance, considere `<link rel="preconnect">` e `<link href="..." rel="stylesheet">` no `head`.
- **Links sociais**: botões GitHub/LinkedIn no herói; cartões de projetos apontam para repositórios externos.

## Tarefas Comuns (Exemplos)
- **Adicionar projeto**: duplique `.project-card` em [index.html](index.html) na seção `#projects`, mantendo `.project-btn`.
- **Adicionar habilidade**: acrescente um `.skill-card` dentro de `.skills-container` em `#skills`.
- **Ajustar tema**: altere variáveis em [assets/css/style.css](assets/css/style.css); evite mexer em muitas regras individuais.
- **Aprimorar JS**: mantenha leve em [assets/js/main.js](assets/js/main.js); sem dependências. Ex.: scroll spy simples ou melhorias de acessibilidade.

## Organização de Arquivos
- **Novas imagens**: coloque em [assets/img/](assets/img) e referencie por caminhos relativos.
- **Novo CSS/JS**: prefira estender arquivos existentes. Se criar novos, inclua com `<link>` ou `<script>` em [index.html](index.html).

## Desempenho e SEO
- **Minimizar**: mantenha CSS/JS pequenos; evite bibliotecas pesadas.
- **Meta**: considere `meta` descritivos (description, Open Graph) ao atualizar o `head`.
- **Responsivo**: preserve boa experiência em telas estreitas.

## Segurança e Estilo
- **Sem frameworks**: não adicione React/Vue/Bootstrap sem autorização explícita.
- **Consistência**: siga o estilo visual e semântico atual.
- **Direitos autorais**: não inclua cabeçalhos de licença sem pedido.

Se algo estiver ambíguo ou incompleto (ex.: configurações de Pages, meta preferidos), avise qual seção precisa esclarecimento para que eu refine.
>>>>>>> 27c59e431fa43d2f462823963f9871136e79887c
