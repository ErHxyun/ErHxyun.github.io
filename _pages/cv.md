---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 4
---

{% assign cv_url = "/assets/pdf/Xiyun_Hu_CV.pdf" | relative_url %}

<div class="cv-pdf-actions">
  <a href="{{ cv_url }}" target="_blank" rel="noopener"><i class="fa-solid fa-up-right-from-square"></i> Open in new tab</a>
  <a href="{{ cv_url }}" download><i class="fa-solid fa-file-arrow-down"></i> Download PDF</a>
</div>

<object class="cv-pdf" data="{{ cv_url }}#view=FitH" type="application/pdf">
  <p>Your browser can't display the PDF here. <a href="{{ cv_url }}">Open the CV</a> instead.</p>
</object>
