from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup


class SeleniumElementsActions:
    @staticmethod
    def only_wait(driver, by_1, by_2, value_1, value_2):
        try:
            element = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((by_1, value_1))
            )

            return element
        except Exception as e:
            element = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((by_2, value_2))
            )

            return element

        except BaseException:
            print(f"Erro ao esperar elemento: {value_1} e {value_2}")
            return None

    @staticmethod
    def wait_and_click(driver: object, by_1: object, by_2: object, value_1: object, value_2: object) -> object:
        try:
            element = WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((by_1, value_1))
            )
            element.click()
            return element

        except Exception as e:
            element = WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((by_2, value_2))
            )
            element.click()
            return element

        except BaseException:
            print(f"Erro ao clicar no elemento: {value_1} e {value_2}")
            return None
    @staticmethod

    def wait_and_click_teste(driver: object, by: object,  value:object) -> object:

        element = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((by, value))
        )
        element.click()
        return element

    def wait_and_send_keys(driver: object, keys: object, by: object, value_1: object, value_2: object):

        try:
            element = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((by, value_1))
            )
            element.send_keys(keys)
            return element

        except Exception as e:
            element = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((by, value_2))
            )
            element.send_keys(keys)

        except BaseException:
            print(f"Erro ao enviar as teclas para o elemento: {value_1} e {value_2}")
            return None

    @staticmethod
    def find_element(driver: object, by: object, value_1: object, value_2: object):
        element = SeleniumElementsActions.only_wait(driver, by, value_1, value_2)
        if element:
            try:
                return element.find_elements(
                    by=by,
                    value=value_1
                )
            except Exception as e:
                return element.find_elements(
                    by=by,
                    value=value_2
                )
            except BaseException:
                print(f"Erro ao encontrar o elemento: {value_1} e {value_2}")


class BeautifulSoupActions:
    @staticmethod
    def find_elements_by_tag(html_content, tag_name):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all(tag_name)

    @staticmethod
    def find_element_by_id(html_content, id):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find(id=id)

    @staticmethod
    def find_element_by_class(html_content, class_name):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find(class_=class_name)

    @staticmethod
    def get_element_text(element):
        return element.get_text()

    @staticmethod
    def get_element_attribute(element, attribute_name):
        return element.get(attribute_name)

    @staticmethod
    def find_element_within_element(parent_element, tag_name):
        return parent_element.find(tag_name)