# Game-Simulator-supported-w-bluestack-5

This project simulates a **game controller using a physical dummy gun**, enabling the user to interact with shooting games (e.g., PUBG Mobile, Free Fire, Call of Duty Mobile) on **Bluestacks** (Android emulator for PC). The dummy gun acts as a real trigger device, mapped to keyboard inputs using **Arduino Uno** and **Python scripting**.

---

## 🎮 Project Overview

A **dummy gun** is connected to an **Arduino Uno**, which detects the trigger action (usually via a push button or sensor). The signal is sent over USB serial communication to a **Python script**, which simulates keyboard presses using the `pyautogui` or `pynput` library. These key presses are pre-mapped in **Bluestacks' key mapping tool** to trigger in-game actions like shooting, aiming, or reloading.

---

## 🧰 Components Required

* Arduino Uno
* Push button (simulates the gun trigger)
* USB cable (for Arduino)
* Dummy gun frame (3D printed, cardboard, or toy)
* PC with Bluestacks installed
* Python 3.x
* Python Libraries: `pyserial`, `pyautogui` or `pynput`

---

## ⚙️ Working Principle

1. **Trigger Mechanism**:
   A push button is fixed inside the dummy gun's trigger area. When pulled, it completes a circuit connected to a digital input pin of Arduino Uno.

2. **Serial Communication**:
   Arduino sends a serial message (like `'SHOOT\n'`) to the PC whenever the trigger is pressed.

3. **Python Listener**:
   A Python script runs on the PC, continuously listens to the Arduino's serial output, and converts it to a virtual keyboard input (e.g., key `"F"` for shooting).

4. **Bluestacks Key Mapping**:
   In Bluestacks, the in-game **fire button** is mapped to the key `"F"`. When Python simulates pressing `"F"`, it simulates the gun firing in the game.

---

## 🔁 Data Flow Diagram

```
Dummy Gun Trigger → Arduino Uno → Serial Port → Python Script → Virtual Key Press → Bluestacks Game Action
```

> Make sure Python has `pyserial` and `pynput` installed:

```bash
pip install pyserial pynput
```

---

## 🕹️ Bluestacks Key Mapping Setup

1. Launch Bluestacks and open your desired game (e.g., PUBG Mobile).
2. Open **Key Mapping Editor**.
3. Map **"Fire"** or **"Shoot"** to the keyboard key `"F"`.
4. Save the keymap.

Now, when the trigger is pressed, Python sends `"F"` and the game registers it as a gunshot.

---

## 📌 Notes

* Debounce may be required in both Arduino and Python to prevent rapid unintended firing.
* You can expand the system to add more buttons for scope, reload, or jump.
* Works best with FPS/TPS games that support keyboard mapping.

---

## 🛠️ Possible Enhancements

* Add a **gyroscope or accelerometer** for aiming.
* Use a **Bluetooth module (e.g., HC-05)** for wireless operation.
* Design a **custom GUI** for configuring keys.

---

## 📄 License

This project is open-source under the MIT License and intended for educational and non-commercial use.

---

## 📷 Demo & Schematic

(Drop any circuit diagram, photos, or demo video links here if available.)

---

Let me know if you'd like the **circuit diagram**, **gun design template**, or **Bluestacks keymap JSON export**!
