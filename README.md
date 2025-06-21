# 🦊 Fox Video Download

**Fox Video Download** é um aplicativo com interface gráfica (Tkinter) para baixar vídeos de diversas plataformas, utilizando a biblioteca [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
O app foi criado para facilitar o download de vídeos para fins **educacionais**.

---

## ✨ Funcionalidades

- Interface gráfica moderna e intuitiva (Tkinter)
- Download de vídeos a partir de uma URL
- Escolha da pasta de destino dos vídeos
- Barra de progresso do download
- Detecção automática de links na área de transferência
- Lista de arquivos baixados na pasta selecionada
- `ffmpeg` embutido no executável (não precisa instalar separadamente)

---
## Como usar com Poetry e rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gehmac/fox-video-download.git
cd fox-video-download
```

### 2. Instale o Poetry

> Siga as instruções oficiais: https://python-poetry.org/docs/#installation

### 3. Instale as dependências

> Recomendado: Use Python 3.12

```bash
poetry install
```

### 4. Execute o app

```bash
poetry run start
```


----
Observações

⚠️ Este projeto é apenas para uso educacional. Não utilize para baixar conteúdos protegidos por direitos autorais sem permissão. 