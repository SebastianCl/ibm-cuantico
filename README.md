# Proyecto de Computación Cuántica con IBM Qiskit

Este proyecto contiene ejemplos básicos de programación cuántica utilizando IBM Qiskit, diseñados para aprender los conceptos fundamentales de la computación cuántica.

## 📋 Contenido del Proyecto

- **`qubit1-1.py`**: Ejemplo básico con un qubit en superposición usando la puerta Hadamard
- **`qubit2-2.py`**: Ejemplo de entrelazamiento cuántico (entanglement) con dos qubits
- **`set-api-key.py`**: Configuración de la API key para acceder a los servicios de IBM Quantum
- **`requirements.txt`**: Dependencias necesarias del proyecto

## 🚀 Requisitos Previos

- Python 3.8 o superior
- Una cuenta en [IBM Quantum](https://quantum-computing.ibm.com/)
- API key de IBM Quantum (gratuita)

## 📦 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd ibm-cuantico
   ```

2. **Crea un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En Linux/macOS
   source venv/bin/activate
   ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuración de IBM Quantum

1. **Obtén tu API key:**
   - Regístrate en [IBM Quantum](https://quantum-computing.ibm.com/)
   - Ve a tu perfil y copia tu API token

2. **Configura la API key:**
   - Edita el archivo `set-api-key.py`
   - Reemplaza `"TU_API_KEY_AQUI"` con tu token real
   - Ejecuta el script:
   ```bash
   python set-api-key.py
   ```

## 🎯 Ejemplos Incluidos

### 1. Qubit Simple (qubit1-1.py)

Demuestra los conceptos básicos de:
- Creación de un circuito cuántico
- Aplicación de la puerta Hadamard para crear superposición
- Medición de qubits
- Simulación local

```bash
python qubit1-1.py
```

**Salida esperada:** Aproximadamente 50% de resultados '0' y 50% de resultados '1'

### 2. Entrelazamiento Cuántico (qubit2-2.py)

Demuestra:
- Circuito con múltiples qubits
- Creación de entrelazamiento usando puertas CNOT
- Correlaciones cuánticas

```bash
python qubit2-2.py
```

**Salida esperada:** Solo estados '00' y '11' (estados entrelazados)

## 📊 Conceptos Cuánticos Ilustrados

### Superposición
Los qubits pueden existir en una combinación de estados |0⟩ y |1⟩ simultáneamente, a diferencia de los bits clásicos.

### Entrelazamiento
Dos o más qubits pueden estar correlacionados de tal manera que el estado de uno afecta instantáneamente al otro, sin importar la distancia.

### Medición
Al medir un qubit, colapsa de su estado de superposición a un estado clásico definido (0 o 1).

## 🛠️ Dependencias

- **qiskit (2.1.2)**: Framework principal de computación cuántica
- **qiskit-aer (0.15.1)**: Simuladores cuánticos de alto rendimiento
- **numpy (2.3.2)**: Computación numérica
- **scipy (1.16.1)**: Algoritmos científicos

## 📈 Próximos Pasos

Para expandir tu conocimiento en computación cuántica, considera explorar:

1. **Algoritmos cuánticos clásicos:**
   - Algoritmo de Grover (búsqueda cuántica)
   - Algoritmo de Shor (factorización)
   - Transformada de Fourier cuántica

2. **Hardware cuántico real:**
   - Ejecutar circuitos en computadoras cuánticas de IBM
   - Análisis de ruido y corrección de errores

3. **Aplicaciones avanzadas:**
   - Optimización cuántica
   - Machine learning cuántico
   - Criptografía cuántica
