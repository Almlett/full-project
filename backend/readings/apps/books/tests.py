
"""
test Serializer, ViewSet, Model
"""
import json
import pytest
from django.urls import reverse
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError
from .models import Genre, Book	# pylint: disable=relative-beyond-top-level
from .serializers import GenreSerializer, BookSerializer	# pylint: disable=relative-beyond-top-level
from .viewsets import GenreViewSet, BookViewSet	# pylint: disable=relative-beyond-top-level

class TestGenreSerializer:
    """
    Test for GenreSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"id": 1, "name": "TEST_TEXT"}

        genre = Genre(**expected_results)
        results = GenreSerializer(genre).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = GenreSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestGenreViewSet:
    """
    Test for GenreViewSet
    """

    @pytest.mark.urls('series.urls')
    def test_list(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test list
        """
        # django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('genre-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            Genre(id = '1', name = 'TEST_TEXT'),
            Genre(id = '1', name = 'TEST_TEXT')
        )

        mocker.patch.object(GenreViewSet, 'get_queryset', return_value=queryset)
        response = GenreViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('series.urls')
    def test_create(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test create
        """
        url = reverse('genre-list')

        data = {"id": 1, "name": "TEST_TEXT"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(Genre, 'save')
        # Renderizamos la vista con nuestro request.
        response = GenreViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('name') == 'TEST_TEXT'
        # Verificamos si efectivamente se llamo el metodo save
        assert Genre.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('genre-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"id": 1, "name": "TEST_TEXT2"}))
        genre = Genre(id = '1', name = 'TEST_TEXT')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Genre

        mocker.patch.object(GenreViewSet, 'get_object', return_value=genre)
        mocker.patch.object(Genre, 'save')

        response = GenreViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'TEST_TEXT2'
        assert Genre.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('genre-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        genre = Genre(id = '1', name = 'TEST_TEXT')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(GenreViewSet, 'get_object', return_value=genre)
        mocker.patch.object(Genre, 'delete')

        response = GenreViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert Genre.delete.called


class TestBookSerializer:
    """
    Test for BookSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"name": "TEST_TEXT", "year": "2020-10-06", "id": 1, "provider": "TEST_TEXT", "genre": "2020-10-06", "pages": "2020-10-06"}

        book = Book(**expected_results)
        results = BookSerializer(book).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = BookSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestBookViewSet:
    """
    Test for BookViewSet
    """

    @pytest.mark.urls('series.urls')
    def test_list(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test list
        """
        # django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('book-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            Book(name = 'TEST_TEXT', year = '2020-10-06', pages = '2020-10-06', provider = 'TEST_TEXT', genre = '2020-10-06', id = '1'),
            Book(name = 'TEST_TEXT', year = '2020-10-06', pages = '2020-10-06', provider = 'TEST_TEXT', genre = '2020-10-06', id = '1')
        )

        mocker.patch.object(BookViewSet, 'get_queryset', return_value=queryset)
        response = BookViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('series.urls')
    def test_create(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test create
        """
        url = reverse('book-list')

        data = {"name": "TEST_TEXT", "year": "2020-10-06", "id": 1, "provider": "TEST_TEXT", "genre": "2020-10-06", "pages": "2020-10-06"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(Book, 'save')
        # Renderizamos la vista con nuestro request.
        response = BookViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('name') == 'TEST_TEXT'
        # Verificamos si efectivamente se llamo el metodo save
        assert Book.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('book-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"name": "TEST_TEXT2", "year": "2019-03-02", "id": 1, "provider": "TEST_TEXT2", "genre": "2019-03-02", "pages": "2019-03-02"}))
        book = Book(name = 'TEST_TEXT', year = '2020-10-06', pages = '2020-10-06', provider = 'TEST_TEXT', genre = '2020-10-06', id = '1')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Book

        mocker.patch.object(BookViewSet, 'get_object', return_value=book)
        mocker.patch.object(Book, 'save')

        response = BookViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'TEST_TEXT2'
        assert Book.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('book-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        book = Book(name = 'TEST_TEXT', year = '2020-10-06', pages = '2020-10-06', provider = 'TEST_TEXT', genre = '2020-10-06', id = '1')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(BookViewSet, 'get_object', return_value=book)
        mocker.patch.object(Book, 'delete')

        response = BookViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert Book.delete.called

