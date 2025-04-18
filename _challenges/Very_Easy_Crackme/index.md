---
title: Very_Easy_Crackme
---

{% capture solution %}
{% include_relative solution.md %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/Very_Easy_Crackme/keygen.py" | first %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```

