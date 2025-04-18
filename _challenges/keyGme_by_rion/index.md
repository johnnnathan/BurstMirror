---
title: Keygme_By_Rion
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/keyGme_by_rion/keygen.c" %}
## 🔑 Keygen (C)

```c
{% include_relative keygen.c%}
```
{% endif %}
