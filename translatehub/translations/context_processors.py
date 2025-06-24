from .config import SocialMedia


def footer_context(request):
    footer_data = {
        'instagram_link' : SocialMedia.INSTAGRAM_LINK,
        'twitter_link'   : SocialMedia.TWITTER_LINK,
        'telegram_link'  : SocialMedia.TELEGRAM_LINK,
        'vkontakte_link' : SocialMedia.VKONTAKTE_LINK,
        'youtube_link'   : SocialMedia.YOUTUBE_LINK,
        'github_link'    : SocialMedia.GITHUB_LINK
    }
    return footer_data