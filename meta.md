---
title: Survey Variables
layout: page
---

---

{% for var in site.data.pulsemeta %}

## {{ var[1].name }}

**Codename**: {{ var[0] }}

**Data Type**: {{ var[1].type }}

**Question Text**:

> {{ var[1].question_text }}

**Response Options**:

{% for item in var[1].options %}> - {{ item[0] }}: {{ item[1] }}
{% endfor %}

---

{% endfor %}

