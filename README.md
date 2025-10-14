# Saúde 60+RS — IVCF-20 + Painel IA (Frontend independente)

Interface leve (HTML único) para atenção à pessoa idosa: **calculadora IVCF-20**, **recomendações automáticas**, **tema claro/escuro**, **exportação/importação JSON** e **relatório imprimível com assinaturas**. Zero dependências de servidor.

## ✨ Recursos
- **IVCF-20 completo** (itens 1–20 + subitens; IMC automático).
- **Classificação** Baixa (0–6), Moderada (7–14), Alta (≥15).
- **Recomendações dinâmicas**: quedas/marcha, cognição, humor, visão/audição, nutrição/sarcopenia, polifarmácia, internação.
- **Campos do projeto**: município, UBS/ESF, profissional, CNS/CPF, paciente e data.
- **Exportar/Importar JSON**, **Imprimir/PDF**, **tema escuro**.
- **UI** glass/neumórfica, responsiva, sem dependências externas (apenas fonte Google).

## 🚀 Como usar
1. Baixe o arquivo `index.html` e abra no navegador.
2. Preencha os campos do cabeçalho e responda ao IVCF-20 (marque **Sim** somente quando houver declínio).
3. Veja o **escore**, a **categoria** e as **recomendações**.
4. Use **Exportar JSON** para salvar o atendimento ou **Importar JSON** para reabrir.
5. Clique em **Imprimir** para gerar a via com **linhas de assinatura**.

> Dica: todo o estado fica no `localStorage` (offline). O JSON exportado contém apenas o atendimento corrente.

## 📦 Desenvolvimento
- O projeto é **estático** (HTML/CSS/JS). Basta editar `index.html`.
- Padrão de *commit* sugerido: Conventional Commits (`feat:`, `fix:`, `docs:`, etc.).

### Scripts úteis (opcional)
```bash
# servidor local simples (Python 3)
python -m http.server 8080
