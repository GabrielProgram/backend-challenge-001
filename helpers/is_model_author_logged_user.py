def is_model_author_logged_user(model, request):
    return model is not None and model.author.pk == request.user.pk