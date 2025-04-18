---
title: Keygme_By_Rion
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/keyGme_by_rion/keygen.py" | first %}
## 🔑 Keygen (C)

```c
{% include_relative keygen.c%}
```
