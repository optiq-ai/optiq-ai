# Sandbox – HTML/JS Runner

Ten folder zawiera lokalny sandbox do uruchamiania kodu HTML/JS z poziomu aplikacji.

## Jak działa:
- Frontend generuje kod
- Tworzy `Blob` z HTML-em
- Ładuje go do `iframe` z `sandbox/index.html`
- `index.html` odbiera `window.postMessage()` i renderuje kod

## Obsługiwane języki:
- JavaScript (module)
- HTML

**Nie obsługuje backendu ani Reacta SSR.**
