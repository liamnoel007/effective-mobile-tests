# Effective Mobile — UI Тесты

**5 автотестов** навигации по сайту [effective-mobile.ru](https://effective-mobile.ru)  
**Playwright + Python + Allure + Docker Compose**

---

## Что проверяется

| Тест         | URL         | Заголовок         |
| ------------ | ----------- | ----------------- |
| **О нас**    | `#about`    | `О нас`           |
| **Услуги**   | `#moreinfo` | `услуги`          |
| **Проекты**  | `#cases`    | `проекты`         |
| **Отзывы**   | `#Reviews`  | `ОТЗЫВЫ КЛИЕНТОВ` |
| **Контакты** | `#contacts` | `контакты`        |

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
git clone https://github.com/ТВОЙ_ЛОГИН/effective-mobile-tests.git
cd effective-mobile-tests
```
