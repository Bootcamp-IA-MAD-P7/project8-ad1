# Plan: adquisición y registro de los datos originales

## Especificación relacionada

- `specs/001-data-foundation/spec.md`

## Situación actual

El repositorio original no incluía archivos de datos. Las consignas proporcionaban
una carpeta compartida de Google Drive con CSV, documentos de Google Sheets y un
archivo derivado de Power BI.

Se decidió trabajar con todas las ciudades disponibles. La adquisición comenzó
antes de crear esta especificación, lo que supone una desviación del flujo SDD.
La trazabilidad se corrige antes de realizar el commit y queda documentada de
forma explícita.

Actualmente existen seis CSV originales en `data/raw/airbnb/`, junto con un
README de procedencia y un manifiesto de integridad.

## Enfoque propuesto

Utilizar como fuentes los seis CSV que ofrecen cobertura uniforme para todas las
ciudades.

Los datos se conservan en una carpeta `raw`, sin modificaciones. La procedencia,
autorización y reglas de uso se explican en `data/README.md`.

Un manifiesto estructurado registra la ruta, el tamaño y la huella SHA-256 de
cada archivo. Esto permite detectar modificaciones accidentales.

Los CSV se incluirán en Git convencional porque su redistribución está autorizada
y ningún archivo requiere Git LFS.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `data/README.md` | Documentar fuente, autorización, alcance y reglas de conservación | REQ-002, REQ-003, REQ-006 |
| `data/manifest.csv` | Registrar tamaño, ruta y huella SHA-256 | REQ-004 |
| `data/raw/airbnb/\*.csv` | Conservar los seis datasets originales | REQ-001, REQ-002 |
| `specs/001-data-foundation/spec.md` | Definir alcance y criterios de aceptación | REQ-001 a REQ-006 |
| `specs/001-data-foundation/plan.md` | Documentar la estrategia de adquisición | REQ-001 a REQ-006 |
| `specs/001-data-foundation/tasks.md` | Registrar ejecución, validaciones y progreso | REQ-001 a REQ-006 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Listar `data/raw/airbnb/\*.csv` | Existen exactamente seis CSV | AC-001, AC-006 |
| Comparar tamaños | Ningún archivo está vacío y los tamaños coinciden con la descarga | AC-001 |
| Leer las cabeceras | Los seis archivos son CSV reales y no páginas HTML | AC-001 |
| Recalcular SHA-256 | Las huellas coinciden con `data/manifest.csv` | AC-004, AC-005 |
| Revisar `data/README.md` | Fuente, autorización y reglas están documentadas | AC-002, AC-003, AC-007 |
| Revisar `git status --short` | Solo aparecen los archivos previstos | AC-006, AC-008 |
| Ejecutar `python scripts/validate\_specs.py` | Todas las especificaciones son válidas | AC-008 |

## Riesgos y alternativas

- Los esquemas tienen entre 14 y 16 columnas. La unión se pospone hasta realizar
  un inventario técnico.
- Los archivos proceden de fechas diferentes. Todavía no se realizarán
  comparaciones temporales.
- Algunos campos pueden identificar anfitriones o ubicaciones. Las conclusiones
  posteriores deben presentarse de forma agregada.
- Excluir los CSV de Git reduciría el tamaño del repositorio, pero dificultaría
  la reproducción inmediata. Se incluyen porque existe autorización y su tamaño
  es razonable.
- Git LFS añadiría complejidad sin aportar valor para archivos de este tamaño.

## Secuencia

1\. Descargar los seis CSV.
2\. Conservarlos en `data/raw/airbnb/`.
3\. Documentar fuente, autorización y reglas de conservación.
4\. Calcular tamaños y huellas SHA-256.
5\. Crear y revisar `data/manifest.csv`.
6\. Preparar exclusivamente los archivos previstos en Git.
7\. Completar la documentación SDD.
8\. Ejecutar el validador.
9\. Revisar el commit antes de integrarlo.
