---
title: third_by_Jenya 
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/third_by_Jenya/keygen.py" | first %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
