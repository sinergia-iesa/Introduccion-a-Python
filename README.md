# Introducción a Python

Presentación en [Slidev](https://sli.dev/) con lo básico para empezar a programar
en Python desde cero: variables, tipos de datos, operadores, condicionales,
ciclos y listas. En vez de capturas de pantalla, cada concepto se explica con
un bloque de código mínimo.

## Desarrollo local

```bash
npm install
npm run dev   # abre la presentación en http://localhost:3030
```

## Despliegue

Se despliega automáticamente a GitHub Pages con GitHub Actions al hacer push
a `main` (ver `.github/workflows/deploy.yml`). La URL queda bajo
`https://<usuario>.github.io/<nombre-del-repo>/`.

## Estructura

```
Introduccion-a-Python/
├── slides.md                    → portada + tabla de contenidos
├── pages/
│   └── introduccionAPython.md   → contenido: variables, tipos, operadores,
│                                   condicionales, ciclos, listas
├── setup/
│   └── shiki.ts                 → tema de resaltado de código (Dracula)
├── styles.css                   → identidad visual (colores, tipografías)
└── public/                      → portada y logos institucionales
```
