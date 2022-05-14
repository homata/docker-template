from django.shortcuts import render
import traceback

import logging
logger = logging.getLogger(__file__)


def index(request):
    """
    トップページ

    Parameters
    ----------
    request : object
        Request オブジェクト

    Returns
    -------
    render : object
        Render オブジェクト

    Notes
    -----
    今は、空ページを返す
    """

    contexts = {}

    if request.user.is_authenticated:
        contexts['user'] = {"username": request.user.username, "is_authenticated": True}

    try:
        return render(request, 'apps/index.html', contexts)
    except Exception as e:
        logger.error(e)
        return render(request, 'apps/index.html', {})
    except:
        traceback.print_exc()
        return render(request, 'apps/index.html', {})
