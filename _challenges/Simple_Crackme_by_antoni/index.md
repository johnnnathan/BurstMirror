---
title: Simple_Crackme_By_Antoni
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/Simple_Crackme_by_antoni/keygen.py" | first %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
