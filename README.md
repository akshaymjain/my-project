# 🧮 3D AI Geometry Chalkboard

An interactive 3D geometry assistant and calculation chalkboard designed to compute key geometric properties for seven major three-dimensional shapes. Built with a focus on mathematical accuracy, structured logic, and ease of use.

---

## ✨ Features

* **Comprehensive Shape Support:** Handles calculations for **7 distinct 3D shapes**:
  * **Cube**
  * **Cuboid**
  * **Cylinder**
  * **Cone**
  * **Frustum** (including slant height, curved surface area, total surface area, and volume)
  * **Sphere**
  * **Hemisphere**
* **Multi-Property Calculations:** Computes Surface Area (Curved/Lateral & Total), Volume, Diagonal lengths, and Slant Heights depending on the selected shape.
* **Interactive Chalkboard Workflow:** Guides the user cleanly through selecting shapes, entering dimensions, and viewing formatted results.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Concepts:** Mathematical Modeling, Conditional Logic, User Input Handling, Modular Functions

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system. You can check by running:
```bash
python --version
```

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project folder:**
   ```bash
   cd my-project
   ```

3. **Run the application:**
   ```bash
   python geometryai.py
   ```

---

## 📐 Supported Shapes & Formulas Overview

| Shape | Inputs Required | Calculated Outputs |
| :--- | :--- | :--- |
| **Cube** | Side ($a$) | Lateral Surface Area, Total Surface Area, Volume, Space Diagonal |
| **Cuboid** | Length ($l$), Breadth ($b$), Height ($h$) | Lateral Surface Area, Total Surface Area, Volume, Diagonal |
| **Cylinder** | Radius ($r$), Height ($h$) | Curved Surface Area, Total Surface Area, Volume |
| **Cone** | Radius ($r$), Height ($h$) | Slant Height ($l$), Curved Surface Area, Total Surface Area, Volume |
| **Frustum** | Top Radius ($r_1$), Bottom Radius ($r_2$), Height ($h$) | Slant Height ($l$), Curved Surface Area, Total Surface Area, Volume |
| **Sphere** | Radius ($r$) | Surface Area, Volume |
| **Hemisphere** | Radius ($r$) | Curved Surface Area, Total Surface Area, Volume |

---

## 🔮 Future Roadmap

* [ ] Add 3D visual wireframe plotting using `matplotlib` or `plotly`.
* [ ] Integrate an LLM API to parse natural-language geometry word problems automatically.
* [ ] Add unit conversion support (cm, m, inches, feet).
* [ ] Build a web-based UI for easier sharing.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   