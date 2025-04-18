---
title: My_First_Crackme_By_None404
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/My_First_Crackme_by_None404/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
{% endif %}
