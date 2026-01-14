<!-- 60-Day Time Management Logbook — one day per A4 page (tight layout) -->
<!-- Tight A4 CSS to fit one day per page -->
<style>
@page { size: A4; margin: 10mm; }

/* Ensure each day block occupies one printable page */
.day-page {
  box-sizing: border-box;
  display: block;
  page-break-after: always;
  /* content box height = A4 height (297mm) minus top+bottom margins (2*10mm) */
  height: calc(297mm - 20mm);
  overflow: hidden;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10px;
  line-height: 1.05;
}

/* Compact header */
.day-title {
  font-size: 12px;
  font-weight:700;
  margin: 0 0 4px 0;
}

/* Dense table */
.log-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9.25px;
}
.log-table th, .log-table td {
  border: 1px solid #333;
  padding: 2px 4px;
  vertical-align: middle;
}
.log-table th {
  background: #f4f4f4;
  font-weight:700;
  font-size: 9.5px;
}
.log-table td { height: 10px; }

/* Tight review and boxes */
.section-title { font-weight:700; margin-top:6px; margin-bottom:4px; font-size:10px; }
.box {
  border: 1px dashed #333;
  padding: 6px;
  min-height: 28px;
  font-size: 9.25px;
  overflow: hidden;
}

/* Signature row compressed */
.signature-line {
  margin-top: 8px;
  display:flex;
  justify-content:space-between;
  font-size: 9px;
}
.signature-line .left { width: 45%; border-top: 1px solid #333; text-align:left; padding-top:4px; }
.signature-line .right { width: 45%; border-top: 1px solid #333; text-align:right; padding-top:4px; }

/* Checklist - small and compact */
.checklist { margin-top: 6px; font-size: 9px; }
.checklist ul { margin: 2px 0 0 16px; padding:0; }

/* Reduce list spacing */
.day-page ul { margin: 0 0 0 14px; padding: 0; }
.day-page li { margin: 2px 0; }

/* Force no page breaks inside the day content */
.day-page, .day-page * { break-inside: avoid; -webkit-column-break-inside: avoid; }

/* Slightly reduce spacing in table header */
.log-table thead th { padding-top:2px; padding-bottom:2px; }
</style>


<div class="day-page">
  <div class="day-title">Tuesday, 16 September 2025  &nbsp;&nbsp;  Day 1 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 17 September 2025  &nbsp;&nbsp;  Day 2 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 18 September 2025  &nbsp;&nbsp;  Day 3 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 19 September 2025  &nbsp;&nbsp;  Day 4 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 20 September 2025  &nbsp;&nbsp;  Day 5 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 21 September 2025  &nbsp;&nbsp;  Day 6 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 22 September 2025  &nbsp;&nbsp;  Day 7 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 23 September 2025  &nbsp;&nbsp;  Day 8 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 24 September 2025  &nbsp;&nbsp;  Day 9 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 25 September 2025  &nbsp;&nbsp;  Day 10 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 26 September 2025  &nbsp;&nbsp;  Day 11 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 27 September 2025  &nbsp;&nbsp;  Day 12 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 28 September 2025  &nbsp;&nbsp;  Day 13 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 29 September 2025  &nbsp;&nbsp;  Day 14 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 30 September 2025  &nbsp;&nbsp;  Day 15 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 01 October 2025  &nbsp;&nbsp;  Day 16 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 02 October 2025  &nbsp;&nbsp;  Day 17 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 03 October 2025  &nbsp;&nbsp;  Day 18 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 04 October 2025  &nbsp;&nbsp;  Day 19 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 05 October 2025  &nbsp;&nbsp;  Day 20 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 06 October 2025  &nbsp;&nbsp;  Day 21 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 07 October 2025  &nbsp;&nbsp;  Day 22 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 08 October 2025  &nbsp;&nbsp;  Day 23 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 09 October 2025  &nbsp;&nbsp;  Day 24 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 10 October 2025  &nbsp;&nbsp;  Day 25 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 11 October 2025  &nbsp;&nbsp;  Day 26 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 12 October 2025  &nbsp;&nbsp;  Day 27 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 13 October 2025  &nbsp;&nbsp;  Day 28 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 14 October 2025  &nbsp;&nbsp;  Day 29 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 15 October 2025  &nbsp;&nbsp;  Day 30 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 16 October 2025  &nbsp;&nbsp;  Day 31 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 17 October 2025  &nbsp;&nbsp;  Day 32 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 18 October 2025  &nbsp;&nbsp;  Day 33 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 19 October 2025  &nbsp;&nbsp;  Day 34 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 20 October 2025  &nbsp;&nbsp;  Day 35 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 21 October 2025  &nbsp;&nbsp;  Day 36 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 22 October 2025  &nbsp;&nbsp;  Day 37 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 23 October 2025  &nbsp;&nbsp;  Day 38 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 24 October 2025  &nbsp;&nbsp;  Day 39 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 25 October 2025  &nbsp;&nbsp;  Day 40 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 26 October 2025  &nbsp;&nbsp;  Day 41 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 27 October 2025  &nbsp;&nbsp;  Day 42 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 28 October 2025  &nbsp;&nbsp;  Day 43 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 29 October 2025  &nbsp;&nbsp;  Day 44 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 30 October 2025  &nbsp;&nbsp;  Day 45 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 31 October 2025  &nbsp;&nbsp;  Day 46 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 01 November 2025  &nbsp;&nbsp;  Day 47 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 02 November 2025  &nbsp;&nbsp;  Day 48 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 03 November 2025  &nbsp;&nbsp;  Day 49 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 04 November 2025  &nbsp;&nbsp;  Day 50 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 05 November 2025  &nbsp;&nbsp;  Day 51 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 06 November 2025  &nbsp;&nbsp;  Day 52 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 07 November 2025  &nbsp;&nbsp;  Day 53 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Saturday, 08 November 2025  &nbsp;&nbsp;  Day 54 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Sunday, 09 November 2025  &nbsp;&nbsp;  Day 55 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Monday, 10 November 2025  &nbsp;&nbsp;  Day 56 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Tuesday, 11 November 2025  &nbsp;&nbsp;  Day 57 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Wednesday, 12 November 2025  &nbsp;&nbsp;  Day 58 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Thursday, 13 November 2025  &nbsp;&nbsp;  Day 59 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>

<div class="day-page">
  <div class="day-title">Friday, 14 November 2025  &nbsp;&nbsp;  Day 60 / 60</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:2px 4px;">00:00–01:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">01:00–02:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">02:00–03:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">03:00–04:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">04:00–05:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">05:00–06:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">06:00–07:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">07:00–08:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">08:00–09:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">09:00–10:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">10:00–11:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">11:00–12:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">12:00–13:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">13:00–14:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">14:00–15:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">15:00–16:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">16:00–17:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">17:00–18:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">18:00–19:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">19:00–20:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">20:00–21:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">21:00–22:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">22:00–23:00</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td style="padding:2px 4px;">23:00–24:00</td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
      <li>[ ] Wake by 05:30 / morning routine (hydration, quick stretch)</li>
      <li>[ ] First focused study block — 90+ minutes (Pomodoro)</li>
      <li>[ ] Coding / project work — 60 minutes</li>
      <li>[ ] Active revision (flashcards / MCQs) — 30–45 minutes</li>
      <li>[ ] Physical exercise — 20–40 minutes</li>
      <li>[ ] No social media during deep work</li>
      <li>[ ] Plan tomorrow (3 top priorities)</li>
      <li>[ ] Read / learn something new — 30 minutes</li>
      <li>[ ] Sleep by 23:00 target</li>
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>
