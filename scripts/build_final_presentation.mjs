import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const workspaceDir = process.cwd();
const skillDir = process.env.PRESENTATION_SKILL_DIR;
const artifactToolEntry = process.env.ARTIFACT_TOOL_ENTRY;
const runtimePython = process.env.PRESENTATION_RUNTIME_PYTHON;

if (!path.isAbsolute(skillDir ?? "") || !path.isAbsolute(artifactToolEntry ?? "") || !path.isAbsolute(runtimePython ?? "")) {
  throw new Error("PRESENTATION_SKILL_DIR, ARTIFACT_TOOL_ENTRY and PRESENTATION_RUNTIME_PYTHON must be absolute paths.");
}

const { Presentation, PresentationFile } = await import(pathToFileURL(artifactToolEntry).href);
const { resolvePresentationFont, applyPresentationChartFont, finalizePresentation } = await import(
  pathToFileURL(path.join(skillDir, "container_tools/artifact_tool_utils.mjs")).href,
);

const W = 1280;
const H = 720;
const C = {
  coral: "#FF385C",
  coralDark: "#D90B3E",
  ink: "#222222",
  muted: "#6A6A6A",
  soft: "#FFF7F8",
  pale: "#F7F7F7",
  white: "#FFFFFF",
  line: "#E6E6E6",
  teal: "#00A699",
  blue: "#3B82F6",
  purple: "#7B61A8",
  orange: "#FC642D",
  amber: "#F59E0B",
  green: "#059669",
};

const fontFamily = resolvePresentationFont();
const presentation = Presentation.create({ slideSize: { width: W, height: H } });

function box(slide, x, y, w, h, fill = C.white, radius = 18, line = C.line) {
  return slide.shapes.add({
    geometry: "roundRect",
    position: { left: x, top: y, width: w, height: h },
    fill,
    line: { style: "solid", fill: line, width: line === "none" ? 0 : 1 },
    borderRadius: radius,
  });
}

function text(slide, value, x, y, w, h, size = 24, options = {}) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    position: { left: x, top: y, width: w, height: h },
    fill: "none",
    line: { fill: "none", width: 0 },
  });
  shape.text = value;
  shape.text.style = {
    typeface: fontFamily,
    fontSize: size,
    bold: options.bold ?? false,
    color: options.color ?? C.ink,
    alignment: options.align ?? "left",
    verticalAlignment: options.valign ?? "top",
    autoFit: options.autoFit ?? "shrinkText",
    wrap: "square",
    insets: options.insets ?? { left: 0, right: 0, top: 0, bottom: 0 },
  };
  return shape;
}

function richText(slide, paragraphs, x, y, w, h, size = 22, options = {}) {
  const shape = text(slide, "", x, y, w, h, size, options);
  shape.text.set(paragraphs);
  shape.text.style = {
    typeface: fontFamily,
    fontSize: size,
    color: options.color ?? C.ink,
    autoFit: "shrinkText",
    wrap: "square",
    insets: options.insets ?? { left: 0, right: 0, top: 0, bottom: 0 },
  };
  return shape;
}

function baseSlide(title, section, number) {
  const slide = presentation.slides.add();
  slide.background.fill = C.white;
  text(slide, section.toUpperCase(), 64, 32, 400, 24, 13, { bold: true, color: C.coral });
  text(slide, title, 64, 62, 1130, 62, 36, { bold: true });
  slide.shapes.add({ geometry: "line", position: { left: 64, top: 132, width: 1152, height: 0 }, fill: "none", line: { style: "solid", fill: C.line, width: 1 } });
  text(slide, "Proyecto educativo independiente · Datos de seis ciudades", 64, 686, 800, 18, 11, { color: C.muted });
  text(slide, String(number).padStart(2, "0"), 1168, 684, 48, 18, 11, { color: C.muted, align: "right" });
  return slide;
}

function addKpi(slide, x, y, w, value, label, color = C.coral) {
  box(slide, x, y, w, 118, C.soft, 18, "none");
  text(slide, value, x + 18, y + 16, w - 36, 50, 34, { bold: true, color });
  text(slide, label, x + 18, y + 70, w - 36, 28, 15, { color: C.muted });
}

function addNotes(slide, body, sources) {
  slide.speakerNotes.textFrame.setText(`${body}\n\nFuentes: ${sources}`);
}

// 1. Cover
{
  const slide = presentation.slides.add();
  slide.background.fill = C.soft;
  slide.shapes.add({ geometry: "rect", position: { left: 0, top: 0, width: 20, height: H }, fill: C.coral, line: { fill: "none", width: 0 } });
  text(slide, "ANÁLISIS DE DATOS · AIRBNB", 72, 72, 520, 28, 15, { bold: true, color: C.coral });
  text(slide, "Oferta, posicionamiento\ny calidad en alojamientos", 72, 140, 770, 170, 50, { bold: true });
  text(slide, "EDA de 220.031 anuncios en seis ciudades", 76, 332, 650, 42, 24, { color: C.muted });
  box(slide, 860, 112, 300, 430, C.coral, 28, "none");
  text(slide, "6", 910, 170, 200, 90, 72, { bold: true, color: C.white, align: "center" });
  text(slide, "ciudades", 910, 260, 200, 35, 22, { color: C.white, align: "center" });
  text(slide, "220.031", 900, 350, 220, 58, 40, { bold: true, color: C.white, align: "center" });
  text(slide, "anuncios", 910, 412, 200, 35, 22, { color: C.white, align: "center" });
  text(slide, "Fernanda · Proyecto 8 · 2026", 72, 634, 560, 28, 16, { color: C.muted });
  addNotes(slide, "Presento un análisis exploratorio orientado a dos decisiones: localizar segmentos de oferta que merecen investigación y priorizar registros que requieren revisión de calidad. El alcance es diagnóstico, no mide reservas ni rentabilidad.", "README.md; notebooks/03_exploratory_analysis.ipynb; dashboard/data/airbnb_dashboard.csv");
}

// 2. Business decision
{
  const slide = baseSlide("Dos decisiones concretas, un mismo análisis", "Objetivo", 2);
  text(slide, "¿Dónde conviene investigar?", 84, 174, 480, 42, 28, { bold: true });
  text(slide, "Compara ciudad, barrio y tipo de alojamiento para detectar oferta relevante, precio relativo y actividad aproximada.", 84, 226, 480, 110, 21, { color: C.muted });
  text(slide, "¿Qué registros revisar primero?", 716, 174, 480, 42, 28, { bold: true });
  text(slide, "Señala precios no positivos, estancias mínimas extremas y contradicciones en variables de reseñas.", 716, 226, 480, 110, 21, { color: C.muted });
  box(slide, 84, 380, 480, 165, C.soft, 20, "none");
  text(slide, "30", 110, 410, 120, 62, 46, { bold: true, color: C.coral });
  text(slide, "segmentos candidatos\npara investigación", 242, 408, 280, 82, 21, { bold: true });
  box(slide, 716, 380, 480, 165, "#F4FBFA", 20, "none");
  text(slide, "193", 742, 410, 140, 62, 46, { bold: true, color: C.teal });
  text(slide, "señales de calidad\nen tres reglas prioritarias", 892, 408, 270, 82, 21, { bold: true });
  text(slide, "El resultado prioriza investigación. No prescribe precios ni inversión.", 84, 592, 1112, 38, 22, { bold: true, color: C.coralDark, align: "center" });
  addNotes(slide, "La primera pregunta ayuda a enfocar análisis comercial en combinaciones concretas. La segunda convierte observaciones de calidad en una cola de revisión. Las 193 señales son 50 precios no positivos, 20 estancias mínimas de 1.000 noches o más y 123 inconsistencias entre reseñas y tasa mensual; pueden coexistir reglas sobre un registro.", "dashboard/app.py; dashboard/data/airbnb_dashboard.csv; notebooks/03_exploratory_analysis.ipynb");
}

// 3. Data scope
{
  const slide = baseSlide("Londres concentra casi cuatro de cada diez anuncios", "Datos", 3);
  const chart = slide.charts.add("bar", {
    position: { left: 72, top: 164, width: 760, height: 430 },
    categories: ["London", "New York", "Sydney", "Madrid", "Milan", "Tokyo"],
    series: [{ name: "Anuncios", values: [85068, 48895, 36662, 19618, 18322, 11466], fill: C.coral }],
    barOptions: { direction: "bar", grouping: "clustered", gapWidth: 52 },
    hasLegend: false,
    xAxis: { visible: false, majorGridlines: null },
    yAxis: { textStyle: { fill: C.muted, fontSize: 14 }, line: { style: "solid", fill: C.line, width: 1 } },
    dataLabels: { showValue: true, position: "outEnd", textStyle: { fill: C.ink, fontSize: 13, bold: true } },
    chartFill: C.white,
    plotAreaFill: C.white,
    chartLine: { fill: "none", width: 0 },
    plotAreaLine: { fill: "none", width: 0 },
  });
  applyPresentationChartFont(chart, { fontFamily });
  addKpi(slide, 888, 182, 280, "220.031", "anuncios totales");
  addKpi(slide, 888, 326, 280, "6", "archivos CSV / ciudades", C.teal);
  text(slide, "La comparación entre ciudades conserva la ciudad de origen y no mezcla monedas.", 888, 486, 280, 90, 19, { color: C.muted });
  addNotes(slide, "Los seis archivos se unificaron en un solo DataFrame y se añadió la ciudad de origen. Esto permite aplicar el mismo cálculo a todas las ciudades sin perder trazabilidad. Los precios no se comparan directamente entre ciudades porque las monedas no están documentadas en la fuente.", "data/raw/*.csv; notebooks/01_data_inventory.ipynb; notebooks/03_exploratory_analysis.ipynb");
}

// 4. Method
{
  const slide = baseSlide("Del inventario al dashboard sin alterar los archivos originales", "Método", 4);
  const steps = [
    ["1", "Inventario", "Estructura y esquemas"],
    ["2", "Calidad", "59 controles"],
    ["3", "EDA", "Distribuciones y segmentos"],
    ["4", "Contrastes", "Chi-cuadrado y Mann-Whitney"],
    ["5", "Producto", "Power BI, Dash y Docker"],
  ];
  const xs = [66, 310, 554, 798, 1042];
  for (let i = 0; i < steps.length; i += 1) {
    const [n, label, detail] = steps[i];
    box(slide, xs[i], 204, 172, 220, i === 4 ? C.soft : C.pale, 22, "none");
    text(slide, n, xs[i] + 56, 226, 60, 60, 38, { bold: true, color: i === 4 ? C.coral : C.teal, align: "center" });
    text(slide, label, xs[i] + 16, 304, 140, 34, 22, { bold: true, align: "center" });
    text(slide, detail, xs[i] + 16, 350, 140, 52, 15, { color: C.muted, align: "center" });
    if (i < steps.length - 1) {
      slide.shapes.add({ geometry: "line", position: { left: xs[i] + 180, top: 314, width: 52, height: 0 }, fill: "none", line: { style: "solid", fill: C.coral, width: 3 } });
    }
  }
  addKpi(slide, 250, 500, 230, "42", "controles superados", C.green);
  addKpi(slide, 525, 500, 230, "17", "observaciones", C.amber);
  addKpi(slide, 800, 500, 230, "4/4", "tests automatizados", C.teal);
  addNotes(slide, "El proceso empieza entendiendo la estructura, sigue con controles explícitos, después analiza variables y relaciones, contrasta dos hipótesis y termina en un dashboard reproducible. Los datos originales se mantienen sin cambios. Las observaciones no se eliminaron automáticamente.", "notebooks/01_data_inventory.ipynb; notebooks/02_data_quality.ipynb; notebooks/03_exploratory_analysis.ipynb; notebooks/04_statistical_analysis.ipynb; scripts/validate_specs.py; tests/");
}

// 5. Offer composition
{
  const slide = baseSlide("La vivienda completa domina en las seis ciudades", "Hallazgo 1", 5);
  const chart = slide.charts.add("bar", {
    position: { left: 64, top: 166, width: 820, height: 438 },
    categories: ["London", "Madrid", "Milan", "New York", "Sydney", "Tokyo"],
    series: [
      { name: "Vivienda completa", values: [55.77, 57.67, 74.25, 51.97, 62.51, 65.09], fill: C.coral },
      { name: "Habitación privada", values: [42.18, 39.81, 23.88, 45.66, 35.77, 26.20], fill: C.purple },
      { name: "Habitación compartida", values: [0.74, 1.68, 1.46, 2.37, 1.72, 8.71], fill: C.teal },
      { name: "Habitación de hotel", values: [1.31, 0.85, 0.40, 0, 0, 0], fill: C.amber },
    ],
    barOptions: { direction: "bar", grouping: "percentStacked", gapWidth: 38 },
    hasLegend: true,
    legend: { position: "bottom", overlay: false, textStyle: { fill: C.muted, fontSize: 12 } },
    xAxis: { visible: false, majorGridlines: null },
    yAxis: { textStyle: { fill: C.muted, fontSize: 13 }, line: { style: "solid", fill: C.line, width: 1 } },
    dataLabels: { showValue: false },
    chartFill: C.white,
    plotAreaFill: C.white,
    chartLine: { fill: "none", width: 0 },
    plotAreaLine: { fill: "none", width: 0 },
  });
  applyPresentationChartFont(chart, { fontFamily });
  slide.shapes.add({ geometry: "rect", position: { left: 132, top: 536, width: 740, height: 31 }, fill: C.white, line: { fill: "none", width: 0 } });
  text(slide, "Composición porcentual dentro de cada ciudad", 180, 541, 640, 18, 12, { color: C.muted, align: "center" });
  text(slide, "74,25%", 930, 190, 250, 52, 38, { bold: true, color: C.coral });
  text(slide, "de la oferta de Milán es vivienda completa", 930, 246, 250, 80, 20, { color: C.muted });
  text(slide, "8,71%", 930, 374, 250, 52, 38, { bold: true, color: C.teal });
  text(slide, "de la oferta de Tokio es habitación compartida", 930, 430, 250, 80, 20, { color: C.muted });
  text(slide, "No aparece la categoría hotel en Nueva York, Sydney ni Tokio.", 930, 548, 250, 60, 17, { bold: true });
  addNotes(slide, "La composición cambia por ciudad, aunque la vivienda completa es la categoría mayoritaria en todas. Milán destaca por el peso de vivienda completa. Tokio tiene la mayor proporción de habitaciones compartidas. La ausencia de hotel significa que esa categoría no figura en estos archivos; no demuestra que no exista oferta hotelera real.", "notebooks/03_exploratory_analysis.ipynb, tabla city_room_type_summary");
}

// 6. Candidate segments
{
  const slide = baseSlide("Cuatro segmentos combinan escala, precio relativo y actividad", "Hallazgo 2", 6);
  const headers = ["Ciudad · barrio", "Tipo", "Anuncios", "Índice precio", "Dif. actividad"];
  const rows = [
    ["London · Tower Hamlets", "Vivienda completa", "3.950", "91,67", "+0,14"],
    ["Madrid · Embajadores", "Vivienda completa", "1.634", "88,46", "+0,39"],
    ["Milan · CENTRALE", "Vivienda completa", "495", "92,50", "+0,32"],
    ["Sydney · Auburn", "Vivienda completa", "310", "88,71", "+1,28"],
  ];
  const widths = [342, 240, 150, 180, 180];
  let cursor = 64;
  headers.forEach((h, i) => {
    box(slide, cursor, 174, widths[i], 54, i === 0 ? C.coral : C.ink, 0, "none");
    text(slide, h, cursor + 10, 188, widths[i] - 20, 26, 15, { bold: true, color: C.white, align: i > 1 ? "center" : "left" });
    cursor += widths[i];
  });
  rows.forEach((row, r) => {
    cursor = 64;
    row.forEach((value, i) => {
      const fill = r % 2 === 0 ? C.soft : C.white;
      box(slide, cursor, 228 + r * 66, widths[i], 66, fill, 0, C.line);
      text(slide, value, cursor + 10, 247 + r * 66, widths[i] - 20, 28, 17, { bold: i === 0, align: i > 1 ? "center" : "left" });
      cursor += widths[i];
    });
  });
  text(slide, "Índice 100 = mediana del mismo tipo de alojamiento en la ciudad", 64, 520, 670, 30, 17, { color: C.muted });
  box(slide, 804, 510, 408, 112, "#F4FBFA", 18, "none");
  text(slide, "Lectura correcta", 828, 530, 170, 25, 16, { bold: true, color: C.teal });
  text(slide, "Son candidatos para investigar. No constituyen un ranking de rentabilidad.", 828, 564, 350, 44, 18, { bold: true });
  addNotes(slide, "La regla seleccionó 30 segmentos. Estos cuatro ejemplos de vivienda completa combinan volumen, un precio mediano inferior al baseline de su categoría y una actividad aproximada superior. El índice 91,67 significa que la mediana del segmento equivale al 91,67% de la mediana del mismo tipo en la ciudad. La actividad proviene de reviews_per_month y no equivale a ocupación o reservas.", "notebooks/03_exploratory_analysis.ipynb, tabla segment_candidates; dashboard/data/airbnb_dashboard.csv");
}

// 7. Statistical test
{
  const slide = baseSlide("Las estancias mínimas largas muestran menor actividad en las seis ciudades", "Hallazgo 3", 7);
  const chart = slide.charts.add("bar", {
    position: { left: 60, top: 166, width: 840, height: 438 },
    categories: ["London", "Madrid", "Milan", "New York", "Sydney", "Tokyo"],
    series: [
      { name: "8 noches o menos", values: [0.43, 0.27, 0.14, 0.51, 0.18, 1.83], fill: C.coral },
      { name: "Más de 8 noches", values: [0.07, 0.04, 0.01, 0.09, 0.00, 0.43], fill: C.teal },
    ],
    barOptions: { direction: "column", grouping: "clustered", gapWidth: 48 },
    hasLegend: true,
    legend: { position: "bottom", overlay: false, textStyle: { fill: C.muted, fontSize: 13 } },
    xAxis: { textStyle: { fill: C.muted, fontSize: 12 }, line: { style: "solid", fill: C.line, width: 1 } },
    yAxis: { title: "Mediana de reseñas al mes", min: 0, max: 2, majorUnit: 0.5, numberFormatCode: "0.0", textStyle: { fill: C.muted, fontSize: 12 }, majorGridlines: { style: "solid", fill: C.line, width: 1 } },
    chartFill: C.white,
    plotAreaFill: C.white,
    chartLine: { fill: "none", width: 0 },
    plotAreaLine: { fill: "none", width: 0 },
  });
  applyPresentationChartFont(chart, { fontFamily });
  addKpi(slide, 944, 182, 240, "6/6", "ciudades con diferencia", C.teal);
  addKpi(slide, 944, 324, 240, "Holm", "ajuste por comparaciones", C.purple);
  text(slide, "Efecto moderado", 948, 486, 230, 32, 21, { bold: true, color: C.coralDark });
  text(slide, "London, New York, Sydney y Tokyo. Efecto pequeño en Madrid y Milan.", 948, 528, 230, 80, 17, { color: C.muted });
  addNotes(slide, "Se aplicó Mann-Whitney por ciudad y se ajustaron los p-valores con Holm. En las seis ciudades se rechaza la hipótesis nula y el signo del rango biserial es negativo. La asociación es coherente, pero no demuestra causalidad: las reseñas al mes son solo una aproximación de actividad.", "notebooks/04_statistical_analysis.ipynb; scipy==1.18.1 en requirements.txt");
}

// 8. Data quality
{
  const slide = baseSlide("Tres reglas convierten anomalías en una cola de revisión", "Calidad", 8);
  const imageBytes = await fs.readFile(path.join(workspaceDir, "docs/images/presentation/dashboard-quality.png"));
  slide.images.add({
    blob: imageBytes,
    contentType: "image/png",
    alt: "Página de calidad del dashboard público",
    fit: "cover",
    crop: { left: 0, top: 0.035, right: 0, bottom: 0.50 },
    geometry: "roundRect",
    borderRadius: 16,
    position: { left: 520, top: 160, width: 684, height: 472 },
  });
  addKpi(slide, 70, 174, 380, "50", "precios iguales o inferiores a cero", C.coral);
  addKpi(slide, 70, 316, 380, "20", "estancias mínimas de 1.000+ noches", C.amber);
  addKpi(slide, 70, 458, 380, "123", "reseñas sin tasa mensual", C.teal);
  text(slide, "No se eliminan automáticamente: se revisa el registro y su contexto.", 70, 600, 380, 42, 17, { bold: true });
  addNotes(slide, "El dashboard permite filtrar y localizar cada registro afectado. La estancia mínima máxima observada es 1.125 noches. Estos valores se consideran sospechosos o poco operativos, no errores confirmados. La acción propuesta es validar la fuente antes de corregir o excluir.", "notebooks/02_data_quality.ipynb; notebooks/03_exploratory_analysis.ipynb; dashboard/data/airbnb_dashboard.csv; https://project8-airbnb-dashboard.onrender.com/");
}

// 9. Demo
{
  const slide = baseSlide("La evidencia se puede explorar en un dashboard público", "Demo", 9);
  const imageBytes = await fs.readFile(path.join(workspaceDir, "docs/images/presentation/dashboard-offer.png"));
  slide.images.add({
    blob: imageBytes,
    contentType: "image/png",
    alt: "Página de oportunidades del dashboard público",
    fit: "cover",
    crop: { left: 0, top: 0.035, right: 0, bottom: 0.48 },
    geometry: "roundRect",
    borderRadius: 16,
    position: { left: 64, top: 158, width: 802, height: 486 },
  });
  text(slide, "Ruta de demo", 918, 176, 250, 34, 24, { bold: true });
  richText(slide, [
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Filtrar por ciudad"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Revisar segmentos"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Abrir calidad"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Probar filtro vacío"] },
  ], 918, 232, 260, 176, 20);
  box(slide, 900, 448, 298, 124, C.soft, 18, "none");
  text(slide, "Dash + Docker + Render", 922, 470, 254, 30, 18, { bold: true, color: C.coral });
  const url = text(slide, "project8-airbnb-dashboard\n.onrender.com", 922, 514, 254, 42, 15, { color: C.ink });
  url.text.get("project8-airbnb-dashboard").link = { uri: "https://project8-airbnb-dashboard.onrender.com/", isExternal: true };
  addNotes(slide, "En la demo comienzo por la página de oferta, filtro una ciudad y muestro cómo cambian los indicadores, el gráfico y la tabla. Después abro calidad, selecciono una regla y localizo registros. Finalmente pruebo una combinación sin datos para mostrar el estado vacío controlado. El servicio corre con Dash y Gunicorn dentro de Docker y está desplegado en Render.", "dashboard/app.py; Dockerfile; render.yaml; docs/dashboard-demo.md; https://project8-airbnb-dashboard.onrender.com/");
}

// 10. Conclusion
{
  const slide = baseSlide("El proyecto ya orienta prioridades, pero todavía no mide negocio", "Conclusión", 10);
  box(slide, 70, 174, 535, 350, "#F4FBFA", 22, "none");
  text(slide, "Decisiones que sí respalda", 100, 204, 470, 36, 25, { bold: true, color: C.teal });
  richText(slide, [
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Priorizar segmentos para investigación"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Revisar registros sospechosos"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Contrastar la política de estancia mínima"] },
  ], 100, 270, 450, 170, 21);
  box(slide, 675, 174, 535, 350, C.soft, 22, "none");
  text(slide, "Datos necesarios para avanzar", 705, 204, 470, 36, 25, { bold: true, color: C.coral });
  richText(slide, [
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Reservas, ocupación e ingresos"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Moneda y fecha de extracción"] },
    { bulletCharacter: "•", marginLeft: 18 * 12700, indent: -10 * 12700, runs: ["Histórico, costes y valoraciones"] },
  ], 705, 270, 450, 170, 21);
  text(slide, "Ampliaciones propuestas", 70, 572, 300, 28, 18, { bold: true });
  text(slide, "#24 baseline de ML · #25 clustering · #26 datos externos", 372, 570, 838, 32, 20, { bold: true, color: C.coral });
  text(slide, "Resultado actual: diagnóstico reproducible y defendible para decidir qué investigar primero.", 70, 624, 1140, 34, 22, { bold: true, align: "center" });
  addNotes(slide, "El entregable actual es útil como sistema de priorización y auditoría inicial. No debe usarse todavía para fijar precios, estimar demanda, decidir inversión o afirmar rentabilidad. Las tarjetas 24, 25 y 26 quedan documentadas como ampliaciones, condicionadas a un objetivo de modelado claro y mejores datos de negocio.", "README.md; specs/006-project-delivery/spec.md; GitHub issues #24, #25 y #26");
}

const stagingDir = path.join(workspaceDir, ".presentation-build");
const finalPath = process.env.PRESENTATION_OUTPUT_PATH
  ? path.resolve(process.env.PRESENTATION_OUTPUT_PATH)
  : path.join(workspaceDir, "presentation", "airbnb_offer_analysis_final.pptx");
await fs.mkdir(stagingDir, { recursive: true });
await fs.mkdir(path.dirname(finalPath), { recursive: true });
const candidatePath = path.join(stagingDir, "candidate.pptx");
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);

const result = await finalizePresentation({
  explicitTotalSlideCount: 10,
  requiredNativeTableOwnerSlides: [],
  requiredNativeChartOwnerSlides: [3, 5, 7],
  materializeLiteralChartWorkbooks: true,
  workspaceDir,
  candidatePath,
  finalPath,
  pythonExecutable: runtimePython,
  integrityValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_layout_geometry.py"),
  layoutArgs: [
    "--expected-slide-size-emu", "12192000,6858000",
    "--validate-bullet-geometry",
    "--validate-heading-fit",
  ],
  fontPolicy: { basis: "design", families: [fontFamily] },
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, `${path.basename(finalPath)}.validation.json`),
});

console.log(JSON.stringify({ finalPath, fontFamily, result }, null, 2));
