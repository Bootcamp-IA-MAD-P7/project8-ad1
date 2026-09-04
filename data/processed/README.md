# Datos preparados para el dashboard

Esta carpeta recibe archivos derivados y reproducibles. Los CSV generados no se
versionan para evitar duplicar los datos originales.

Para crear la fuente que utiliza Power BI:

```bash
python scripts/prepare_dashboard_data.py
```

El comando genera `airbnb_dashboard.csv` desde los seis archivos inmutables de
`data/raw/airbnb/`. El resultado conserva una fila por anuncio, añade la ciudad de
origen e incorpora únicamente indicadores y agregados documentados en
`docs/dashboard-design.md`.
