
"""
test Serializer, ViewSet, Model
"""
import json
import pytest
from django.urls import reverse
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError
from .models import Profile, UserMovie, UserBook, UserSerie	# pylint: disable=relative-beyond-top-level
from .serializers import ProfileSerializer, UserMovieSerializer, UserBookSerializer, UserSerieSerializer	# pylint: disable=relative-beyond-top-level
from .viewsets import ProfileViewSet, UserMovieViewSet, UserBookViewSet, UserSerieViewSet	# pylint: disable=relative-beyond-top-level

class TestProfileSerializer:
    """
    Test for ProfileSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"auth_user": "2020-10-06", "viewing_time": "TEST_TEXT", "id": 1, "read_time": "TEST_TEXT"}

        profile = Profile(**expected_results)
        results = ProfileSerializer(profile).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = ProfileSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestProfileViewSet:
    """
    Test for ProfileViewSet
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
        url = reverse('profile-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            Profile(auth_user = '2020-10-06', read_time = 'TEST_TEXT', id = '1', viewing_time = 'TEST_TEXT'),
            Profile(auth_user = '2020-10-06', read_time = 'TEST_TEXT', id = '1', viewing_time = 'TEST_TEXT')
        )

        mocker.patch.object(ProfileViewSet, 'get_queryset', return_value=queryset)
        response = ProfileViewSet.as_view({'get': 'list'})(request).render()

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
        url = reverse('profile-list')

        data = {"auth_user": "2020-10-06", "viewing_time": "TEST_TEXT", "id": 1, "read_time": "TEST_TEXT"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(Profile, 'save')
        # Renderizamos la vista con nuestro request.
        response = ProfileViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('auth_user') == '2020-10-06'
        # Verificamos si efectivamente se llamo el metodo save
        assert Profile.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('profile-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"auth_user": "2019-03-02", "viewing_time": "TEST_TEXT2", "id": 1, "read_time": "TEST_TEXT2"}))
        profile = Profile(auth_user = '2020-10-06', read_time = 'TEST_TEXT', id = '1', viewing_time = 'TEST_TEXT')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Profile

        mocker.patch.object(ProfileViewSet, 'get_object', return_value=profile)
        mocker.patch.object(Profile, 'save')

        response = ProfileViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('auth_user') == '2019-03-02'
        assert Profile.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('profile-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        profile = Profile(auth_user = '2020-10-06', read_time = 'TEST_TEXT', id = '1', viewing_time = 'TEST_TEXT')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(ProfileViewSet, 'get_object', return_value=profile)
        mocker.patch.object(Profile, 'delete')

        response = ProfileViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert Profile.delete.called


class TestUserMovieSerializer:
    """
    Test for UserMovieSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"movie": "TEST_TEXT", "movie_name": "TEST_TEXT", "id": 1, "user": "2020-10-06"}

        usermovie = UserMovie(**expected_results)
        results = UserMovieSerializer(usermovie).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = UserMovieSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestUserMovieViewSet:
    """
    Test for UserMovieViewSet
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
        url = reverse('usermovie-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            UserMovie(movie = 'TEST_TEXT', movie_name = 'TEST_TEXT', id = '1', user = '2020-10-06'),
            UserMovie(movie = 'TEST_TEXT', movie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')
        )

        mocker.patch.object(UserMovieViewSet, 'get_queryset', return_value=queryset)
        response = UserMovieViewSet.as_view({'get': 'list'})(request).render()

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
        url = reverse('usermovie-list')

        data = {"movie": "TEST_TEXT", "movie_name": "TEST_TEXT", "id": 1, "user": "2020-10-06"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(UserMovie, 'save')
        # Renderizamos la vista con nuestro request.
        response = UserMovieViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('user') == '2020-10-06'
        # Verificamos si efectivamente se llamo el metodo save
        assert UserMovie.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('usermovie-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"movie": "TEST_TEXT2", "movie_name": "TEST_TEXT2", "id": 1, "user": "2019-03-02"}))
        usermovie = UserMovie(movie = 'TEST_TEXT', movie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo UserMovie

        mocker.patch.object(UserMovieViewSet, 'get_object', return_value=usermovie)
        mocker.patch.object(UserMovie, 'save')

        response = UserMovieViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('user') == '2019-03-02'
        assert UserMovie.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('usermovie-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        usermovie = UserMovie(movie = 'TEST_TEXT', movie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(UserMovieViewSet, 'get_object', return_value=usermovie)
        mocker.patch.object(UserMovie, 'delete')

        response = UserMovieViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert UserMovie.delete.called


class TestUserBookSerializer:
    """
    Test for UserBookSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"book": "TEST_TEXT", "id": 1, "book_name": "TEST_TEXT", "user": "2020-10-06"}

        userbook = UserBook(**expected_results)
        results = UserBookSerializer(userbook).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = UserBookSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestUserBookViewSet:
    """
    Test for UserBookViewSet
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
        url = reverse('userbook-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            UserBook(book = 'TEST_TEXT', id = '1', book_name = 'TEST_TEXT', user = '2020-10-06'),
            UserBook(book = 'TEST_TEXT', id = '1', book_name = 'TEST_TEXT', user = '2020-10-06')
        )

        mocker.patch.object(UserBookViewSet, 'get_queryset', return_value=queryset)
        response = UserBookViewSet.as_view({'get': 'list'})(request).render()

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
        url = reverse('userbook-list')

        data = {"book": "TEST_TEXT", "id": 1, "book_name": "TEST_TEXT", "user": "2020-10-06"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(UserBook, 'save')
        # Renderizamos la vista con nuestro request.
        response = UserBookViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('user') == '2020-10-06'
        # Verificamos si efectivamente se llamo el metodo save
        assert UserBook.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('userbook-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"book": "TEST_TEXT2", "id": 1, "book_name": "TEST_TEXT2", "user": "2019-03-02"}))
        userbook = UserBook(book = 'TEST_TEXT', id = '1', book_name = 'TEST_TEXT', user = '2020-10-06')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo UserBook

        mocker.patch.object(UserBookViewSet, 'get_object', return_value=userbook)
        mocker.patch.object(UserBook, 'save')

        response = UserBookViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('user') == '2019-03-02'
        assert UserBook.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('userbook-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        userbook = UserBook(book = 'TEST_TEXT', id = '1', book_name = 'TEST_TEXT', user = '2020-10-06')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(UserBookViewSet, 'get_object', return_value=userbook)
        mocker.patch.object(UserBook, 'delete')

        response = UserBookViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert UserBook.delete.called


class TestUserSerieSerializer:
    """
    Test for UserSerieSerializer
    """

    def test_expected_serialized_json(self):	# pylint: disable=no-self-use
        """
        test expected serialized json
        """
        expected_results = {"serie": "TEST_TEXT", "serie_name": "TEST_TEXT", "id": 1, "user": "2020-10-06"}

        userserie = UserSerie(**expected_results)
        results = UserSerieSerializer(userserie).data

        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):	# pylint: disable=no-self-use
        """
        test raise error when missing required field
        """
        incomplete_data = {
            'id':1,
        }

        serializer = UserSerieSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestUserSerieViewSet:
    """
    Test for UserSerieViewSet
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
        url = reverse('userserie-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            UserSerie(serie = 'TEST_TEXT', serie_name = 'TEST_TEXT', id = '1', user = '2020-10-06'),
            UserSerie(serie = 'TEST_TEXT', serie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')
        )

        mocker.patch.object(UserSerieViewSet, 'get_queryset', return_value=queryset)
        response = UserSerieViewSet.as_view({'get': 'list'})(request).render()

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
        url = reverse('userserie-list')

        data = {"serie": "TEST_TEXT", "serie_name": "TEST_TEXT", "id": 1, "user": "2020-10-06"}

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(UserSerie, 'save')
        # Renderizamos la vista con nuestro request.
        response = UserSerieViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('user') == '2020-10-06'
        # Verificamos si efectivamente se llamo el metodo save
        assert UserSerie.save.called

    @pytest.mark.urls('series.urls')
    def test_update(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test update
        """
        url = reverse('userserie-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({"serie": "TEST_TEXT2", "serie_name": "TEST_TEXT2", "id": 1, "user": "2019-03-02"}))
        userserie = UserSerie(serie = 'TEST_TEXT', serie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo UserSerie

        mocker.patch.object(UserSerieViewSet, 'get_object', return_value=userserie)
        mocker.patch.object(UserSerie, 'save')

        response = UserSerieViewSet.as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('user') == '2019-03-02'
        assert UserSerie.save.called

    @pytest.mark.urls('series.urls')
    def test_delete(self, rf, mocker):	# pylint: disable=no-self-use disable=invalid-name
        """
        test delete
        """
        url = reverse('userserie-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        userserie = UserSerie(serie = 'TEST_TEXT', serie_name = 'TEST_TEXT', id = '1', user = '2020-10-06')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(UserSerieViewSet, 'get_object', return_value=userserie)
        mocker.patch.object(UserSerie, 'delete')

        response = UserSerieViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert UserSerie.delete.called

