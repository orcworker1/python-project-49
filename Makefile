
install: #Эта команда полезна при первом клонировании репозитория или после удаления зависимостей
	uv sync


brain-games: #Запуск игры 
	uv run brain-games


build: # Собрать пакет
	uv build

package-install: #Установить пакет 
	uv tool install dist/*.whl