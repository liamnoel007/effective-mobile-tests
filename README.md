# Effective Mobile — UI Тесты

**5 автотестов** навигации по сайту [effective-mobile.ru](https://effective-mobile.ru)  
**Playwright + Python + Allure + Docker Compose**

---

## Запуск на **любом компьютере** (Windows / Linux / macOS)

### 1. Установи Docker Desktop

| ОС          | Ссылка                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------- |
| **Windows** | [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) |
| **Linux**   | `sudo apt install docker.io docker-compose`                                                        |
| **macOS**   | [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) |

> **Windows**: Убедись, что **WSL 2** включён (установщик предложит)

---

### 2. Склонируй и запусти (2 команды)

```bash
git clone https://github.com/liamnoel007/effective-mobile-tests.git
cd effective-mobile-tests
```

---

## Первый запуск

## Windows (PowerShell / CMD)

```bash
docker-compose up --build
```

## Linux / macOS

```bash
docker-compose up --build
```

---

## Быстрый повторный запуск

## Windows (PowerShell / CMD)

```bash
docker-compose up
```

## Linux / macOS

```bash
docker-compose up
```

---

## Готово!

Открой в браузере: http://localhost:8080
