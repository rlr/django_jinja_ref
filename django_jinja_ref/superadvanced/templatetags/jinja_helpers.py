from django_jinja import library


@library.global_function
def superfunction():
    return 'I am a global superfunction.'
