---
title: Simple_But_Not_Simple_By_Jackioye
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/Simple_but_not_simple_by_jackioye/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
{% endif %}
