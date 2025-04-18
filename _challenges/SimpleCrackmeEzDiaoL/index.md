---
title: SimpleCrackmeEzDiaoL 
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/SimpleCrackmeEzDiaoL/keygen.c" %}
## 🔑 Keygen (Python)

```c
{% include_relative keygen.c%}
```
{% endif %}

