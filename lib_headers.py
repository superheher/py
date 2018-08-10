def getHeaders(key):
	names = {'ДД':['Директивный документ','Этап контроля','Обозначение ДД',
					'Размещение ДД в структуре папок ОКБ','Процедура выпуска',
					'Оформление ДД','Соответствие ДД модели данных',
					'Модуль создания ДД','Применяемость','Указание о внедрении/заделе',
					'Согласовано','Примечание','Дата','Проверку выполнил'],
			'ДТЭ':['Обозначение КД / Ревизия-Наименование',
					'Тип объекта','Владелец','Подразделение','Обозначение ДД',
					'Этап контроля','Обозначение / Процедура выпуска',
					'Размещение в структуре папок ОКБ\nВходимость в головную сборку / проект',
					'Соответствие модели данных / Время сохранения',
					'Оформление / Состав ЭМ','Ограничения / WAVE-связи','Масса / Материал / Атрибуты',
					'Геометрия / Допуски','Слои / Ссылочные наборы','Анализ зазоров','Согласовано'
					'Документ на отклонение от требований НД','Дата','Проверку выполнил']}
	return names.get(key)