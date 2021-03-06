"""
test Serializer, ViewSet
"""
import json
import pytest
from django.urls import reverse
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError
from .models import Genre	# pylint: disable=relative-beyond-top-level
from .serializers import GenreSerializer	# pylint: disable=relative-beyond-top-level
from .viewsets import GenreViewSet	# pylint: disable=relative-beyond-top-level


class TestGenreSerializer:
    """
    Test for GenreSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {
            'id': 1,
            'name': 'Comedy',
        }

        genre = Genre(**expected_results)
        results = GenreSerializer(genre).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {

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

    @pytest.mark.urls('footage.urls')
    def test_list(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test list
        """
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('genre-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            Genre(name='Drama'),
            Genre(name='Comedy')
        )

        mocker.patch.object(GenreViewSet, 'get_queryset', return_value=queryset)
        response = GenreViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('footage.urls')
    def test_create(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test create
        """
        url = reverse('genre-list')

        data = {
            'name': 'Comedy',
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(Genre, 'save')
        # Renderizamos la vista con nuestro request.
        response = GenreViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('name') == 'Comedy'
        # Verificamos si efectivamente se llamo el metodo save
        assert Genre.save.called

    @pytest.mark.urls('footage.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('genre-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'Enzo'}))
        genre = Genre(name='Comedy')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Genre

        mocker.patch.object(GenreViewSet, 'get_object', return_value=genre)
        mocker.patch.object(Genre, 'save')

        response = GenreViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'Enzo'
        assert Genre.save.called

    @pytest.mark.urls('footage.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('genre-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        genre = Genre(name='Comedy')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(GenreViewSet, 'get_object', return_value=genre)
        mocker.patch.object(Genre, 'delete')

        response = GenreViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert Genre.delete.called
