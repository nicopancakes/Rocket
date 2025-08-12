import requests
from colorama import init, Fore, Style

init(autoreset=True)

# Thank you user for using this tool, enjoy this with over 3,000 paths!
PATHS = sorted([
    # > administration & login
    "admin", "administrator", "admin1", "admin2", "admin3", "admin4", "admin5", "admin_area", "admin_panel",
    "admin_login", "admin_area/login.php", "admin/account.php", "admin/account", "admincp", "cpanel",
    "cpanel/login.php", "controlpanel", "control_panel", "moderator", "moderator_area", "moderator_login",
    "webadmin", "webmaster", "webmaster/login.php", "manage", "management", "useradmin", "panel",
    "backend", "console", "root", "sysadmin", "sysadministrator", "system", "systems", "administrator/login.php",
    "admin/login", "admin/index.php", "admin.php", "adm", "adm.php", "admin_area.php", "administrator_area.php",

    # > authentication
    "login", "login.php", "login.html", "signin", "signin.php", "signin.html", "logout", "logout.php",
    "logout.html", "register", "register.php", "signup", "signup.php", "password", "password-reset", "forgot",
    "forgot-password", "resetpassword", "changepassword", "change-password", "verify", "verification",
    "confirm", "confirmation",

    # > api 
    "api", "api/v1", "api/v2", "api/v3", "api-docs", "apidocs", "swagger", "swagger-ui", "docs", "documentation",
    "help", "help-center", "support", "support-center", "customer-support", "faq", "knowledgebase", "kb",

    # > user & profile
    "user", "users", "user/profile", "profile", "account", "accounts", "member", "members", "profile-edit",
    "profile-settings", "user-settings", "settings", "preferences", "notifications", "messages", "inbox",
    "chat", "comments", "feedback", "reviews", "ratings", "friends", "followers", "following",

    # > ecom
    "cart", "cart.php", "checkout", "checkout.php", "orders", "order", "billing", "payments", "invoice",
    "invoices", "products", "product", "catalog", "store", "shop", "sale", "discounts", "coupons",

    # > blog
    "blog", "blog-posts", "posts", "articles", "news", "newsletters", "newsletter", "media", "gallery",
    "portfolio", "pages", "page", "home", "index", "default", "landing", "welcome",

    # > files and media
    "files", "uploads", "download", "downloads", "documents", "pdf", "pdfs", "images", "photos", "videos",
    "audio", "music", "media-library", "temp", "tmp", "backup", "backups", "archive", "archives",

    # > system & config
    "config", "config.php", "config.bak", "config_old.php", "settings.php", "license.txt", "readme.md", "readme.html",
    "robots.txt", "sitemap.xml", ".htaccess", "web.config", "error_log", "access_log",

    # analytics
    "seo", "analytics", "stats", "statistics", "tracking", "tags", "pixels",

    # > social etc
    "social", "social-media", "facebook", "twitter", "instagram", "linkedin", "youtube", "pinterest", "reddit",
    "snapchat", "discord", "slack", "chat-rooms",

    # > debug
    "test", "tests", "debug", "debug.php", "phpinfo.php", "error", "error_log", "logs", "log", "console",

    # > cms paths
    "wp-admin", "wp-login.php", "wp-content", "wp-includes", "xmlrpc.php",
    "administrator/index.php", "administrator/login.php", "joomla", "drupal",

    # > common paths
    "ajax", "api2", "app", "apps", "auth", "beta", "cache", "captcha", "cdn", "cms", "contact", "dashboard",
    "database", "db", "download.php", "feed", "feeds", "forum", "forums", "ftp", "git", "gitlab", "helpdesk",
    "home.php", "images.php", "install", "install.php", "jobs", "login.php", "logout.php", "mail", "mailing",
    "maintenance", "marketing", "media.php", "mobile", "myaccount", "news.php", "notification", "oauth",
    "offline", "online", "partners", "password-reset", "payment", "payments.php", "plugins", "privacy",
    "profile.php", "register.php", "reports", "reset-password", "root", "rss", "search", "secure", "security",
    "service", "services", "settings.php", "shop.php", "signup.php", "signin.php", "sms", "social.php",
    "sponsor", "sponsors", "ssl", "staff", "staff-login", "staff-area", "stats.php", "status", "store.php",
    "subscribe", "subscription", "subscriptions", "support.php", "sysadmin", "system.php", "terms", "test.php",
    "themes", "tools", "tracking.php", "translate", "translations", "uploads", "user.php", "users.php",
    "video", "videos.php", "vip", "voice", "web", "webmaster", "webmaster-tools", "widgets", "wiki", "wordpress",

    # > misc
    "adminarea", "adminlogin", "adm", "adm1", "adm2", "adm3", "adm4", "adm5", "adm6", "adm7", "adm8", "adm9",
    "consolepanel", "cp", "cp-login", "cpanel.php", "dashboard.php", "dbadmin", "debugconsole", "devpanel",
    "development", "devtools", "emailadmin", "errorpage", "errors", "eventlog", "fileadmin", "filemanager",
    "forumadmin", "forumlogin", "ftpadmin", "gameserver", "guestbook", "htmladmin", "imagemanager", "imageupload",
    "index.php", "index_old.php", "install", "install.php", "js", "lang", "language", "languages", "login_old.php",
    "maintenance_mode", "mailadmin", "mailbox", "mainadmin", "manager", "managers", "modules", "newsadmin",
    "newsletter", "newsletteradmin", "notifications", "orderadmin", "passwordreset", "permissions", "phpmyadmin",
    "plugin", "plugins", "preferences", "private", "privatearea", "privatefiles", "productadmin", "profileadmin",
    "reportsadmin", "resetpassword", "rssfeed", "rss.xml", "searchadmin", "secureadmin", "serveradmin", "settingsadmin",
    "settingspanel", "shopadmin", "siteadmin", "sitebackup", "siteconfig", "sitemaps", "smtpadmin", "sqladmin",
    "staffadmin", "statisticsadmin", "statuspage", "storeadmin", "systemadmin", "systempanel", "themesadmin",
    "toolsadmin", "trackingadmin", "translateadmin", "translationsadmin", "upload", "uploadadmin", "uploadsadmin",
    "useradmin", "userpanel", "usermanagement", "usermenu", "webadmin", "webmasteradmin", "websiteadmin",
    "webserver", "widgetsadmin", "xmlrpc", "zipadmin",

    # > other
    "api/v1/admin-tools", "api/v1/feature-flags", "api/v1/log-archive", "api/v1/rollouts", "api/v1/sessions",
    "api/v1/tasks", "api/v1/trace", "api/v1/webhook-logs", "api/v1/workflow", "api/v2/admin-tools",
    "api/v2/feature-flags", "api/v2/log-archive", "api/v2/rollouts", "api/v2/sessions", "api/v2/tasks",
    "api/v2/trace", "api/v2/webhook-logs", "api/v2/workflow", "api/beta", "api/internal", "api/v3/admin-tools",
    "api/v3/feature-flags", "api/v3/log-archive", "api/v3/rollouts", "api/v3/sessions", "api/v3/tasks",
    "api/v3/trace", "api/v3/webhook-logs", "api/v3/workflow", "api/auth-tokens", "api/debug", "api/metrics-export",
    "api/metrics/v1", "api/metrics/v2", "api/proxy", "api/usage", "api/v1/deployments", "api/v1/experiments",
    "api/v1/flags", "api/v1/logs/archive", "api/v1/notifications", "api/v1/pipelines", "api/v1/releases",
    "api/v1/rules", "api/v1/services", "api/v1/snapshots", "api/v1/teams", "api/v1/test-results", "api/v1/triggers",
    "api/v1/webhooks", "api/v1/workers", "api/v2/deployments", "api/v2/experiments", "api/v2/flags",
    "api/v2/logs/archive", "api/v2/notifications", "api/v2/pipelines", "api/v2/releases", "api/v2/rules",
    "api/v2/services", "api/v2/snapshots", "api/v2/teams", "api/v2/test-results", "api/v2/triggers",
    "api/v2/webhooks", "api/v2/workers", "api/v3/deployments", "api/v3/experiments", "api/v3/flags",
    "api/v3/logs/archive", "api/v3/notifications", "api/v3/pipelines", "api/v3/releases", "api/v3/rules",
    "api/v3/services", "api/v3/snapshots", "api/v3/teams", "api/v3/test-results", "api/v3/triggers",
    "api/v3/webhooks", "api/v3/workers", "app-config", "app-logs", "app-settings", "artifact-cache",
    "artifact-storage", "audit-logs", "auto-deploy", "auto-scaling", "backup-config", "backup-history",
    "backup-scripts", "backend-api", "beta-features", "build-cache", "build-logs", "build-results",
    "build-triggers", "cache-clear", "cache-invalidate", "cache-status", "ci-artifact-store", "ci-jobs",
    "ci-monitor", "ci-pipeline-status", "ci-queue", "ci-runners", "ci-servers", "ci-snapshots",
    "ci-webhooks", "cli-tools", "cluster-config", "cluster-logs", "cluster-status", "code-analysis",
    "code-coverage", "code-reviews", "code-signing", "config-backups", "config-diffs", "config-repo",
    "config-sync", "config-validator", "console-logs", "container-registry", "container-stats",
    "continuous-deploy", "continuous-integration", "cron-jobs", "cron-logs", "cron-status", "debug-console",
    "debug-logs", "debug-trace", "deploy-history", "deploy-logs", "deploy-status", "deployment-jobs",
    "deployment-logs", "deployment-pipelines", "dev-console", "dev-dashboards", "dev-portal",
    "dev-settings", "dev-tools", "development-logs", "diagnostics", "docker-hub", "docker-images",
    "docker-logs", "docker-monitor", "docker-stats", "docker-volumes", "document-store", "error-tracking",
    "experimental-features", "feature-flag-dashboard", "feature-toggle", "feature-toggles", "feature-tracking",
    "file-storage", "git-hooks", "git-logs", "git-webhooks", "grafana", "grpc-api", "health-dashboard",
    "health-monitor", "health-probes", "healthz", "hook-logs", "hook-monitor", "infrastructure",
    "infrastructure-status", "integration-tests", "internal-api", "internal-dashboard", "internal-docs",
    "internal-tools", "inventory-api", "job-queue", "job-logs", "job-scheduler", "job-status", "jobs-api",
    "key-management", "kibana", "kubernetes-dashboard", "kubernetes-logs", "kubernetes-metrics",
    "lambda-functions", "log-aggregator", "log-collector", "log-dashboards", "log-exporter", "log-monitor",
    "log-processor", "logstash", "machine-learning", "maintenance-scripts", "metrics-api", "metrics-dashboard",
    "metrics-exporter", "metrics-server", "metrics-ui", "migration-scripts", "monitor-dashboard",
    "monitor-logs", "monitoring-api", "monitoring-alerts", "monitoring-dashboards", "monitoring-rules",
    "mysql-backups", "networks", "network-config", "network-logs", "node-status", "notification-center",
    "notification-logs", "notification-settings", "notifications-api", "oauth2-tokens", "observability",
    "openapi", "ops-dashboard", "ops-tools", "operator-dashboard", "operator-tools", "orchestration",
    "package-registry", "pipeline-logs", "pipeline-monitor", "pipeline-ui", "platform-api", "platform-dashboard",
    "platform-tools", "plugin-store", "plugin-updates", "policies", "policy-engine", "policy-rules",
    "post-deploy", "pre-deploy", "preview-environments", "private-api", "process-dashboard",
    "process-monitor", "processes", "profiling-reports", "profiling-tools", "prometheus", "prometheus-alerts",
    "prometheus-metrics", "proxy-logs", "proxy-settings", "pubsub", "queue-monitor", "queue-status",
    "rabbitmq", "release-notes", "release-pipelines", "release-tracking", "repo-status", "repository-hooks",
    "repository-mirror", "resource-monitor", "resource-usage", "rollback-jobs", "rollback-logs",
    "rollback-status", "saml-config", "sandbox-environment", "scheduled-jobs", "schema-registry",
    "script-library", "script-logs", "secret-management", "secret-store", "security-alerts",
    "security-dashboard", "security-events", "security-logs", "security-policies", "self-hosted",
    "service-accounts", "service-discovery", "service-mesh", "service-monitor", "service-status",
    "service-tracing", "session-store", "session-tracking", "settings-api", "shared-storage",
    "shell-access", "shell-scripts", "slack-integration", "source-control", "source-repository",
    "sso-config", "staging-environment", "state-store", "stats-dashboard", "stats-export", "stats-logs",
    "storage-api", "storage-backups", "storage-config", "storage-logs", "storage-monitor", "storage-usage",
    "streaming-api", "system-alerts", "system-backups", "system-health", "system-logs", "system-metrics",
    "system-monitor", "task-queue", "task-scheduler", "test-api", "test-coverage", "test-results",
    "test-runner", "test-suite", "third-party-integrations", "threat-detection", "tls-certs",
    "token-management", "token-refresh", "traffic-analysis", "traffic-monitor", "transaction-logs",
    "transit-encryption", "tracing-api", "tracing-dashboard", "tracing-logs", "triggers-api",
    "ui-dashboard", "ui-settings", "user-activity", "user-logs", "user-roles", "user-settings-api",
    "user-sessions", "version-control", "version-history", "vpc-config", "vulnerability-scans",
    "vulnerability-reports", "webhook-dashboard", "webhook-logs", "webhook-monitor", "webhook-receiver",
    "webhook-tester", "workflow-api", "workflow-jobs", "workflow-logs", "workflow-monitor", "workflow-status",
    "workflow-triggers", "yaml-configs", "zabbix", "zendesk-integration",

    # > other stuff
    "adapters", "alerts-center", "analytics-api", "api-dashboard", "api-keys-management",
    "api-usage-stats", "app-monitoring", "application-logs", "application-status",
    "artifact-management", "artifact-repository", "audit-trail", "authentication-logs",
    "automation", "automation-scripts", "backup-management", "backup-restore",
    "beta-features-dashboard", "build-artifacts", "build-pipelines", "cache-management",
    "cluster-management", "cluster-nodes", "cluster-status-dashboard", "code-insights",
    "code-quality", "code-review-dashboard", "configuration-management", "configuration-store",
    "container-orchestration", "continuous-delivery", "continuous-testing",
    "credential-management", "cron-scheduler", "custom-metrics", "dashboard-api",
    "data-pipelines", "debugging-tools", "deployment-dashboard", "deployment-management",
    "developer-settings", "development-tools", "diagnostics-dashboard", "docker-hub-integration",
    "docker-swarm", "dynamic-config", "edge-network", "error-reporting", "error-tracking-dashboard",
    "event-logging", "feature-flags-management", "feature-management", "feature-toggles-dashboard",
    "file-monitoring", "file-transfer", "git-management", "git-repository", "git-sync",
    "grafana-dashboard", "health-checks", "host-management", "infrastructure-dashboard",
    "integration-dashboard", "integration-management", "integration-tests-dashboard",
    "internal-api-docs", "internal-portal", "iot-dashboard", "issue-tracking",
    "job-queue-dashboard", "job-scheduler-dashboard", "k8s-dashboard", "k8s-logs",
    "lambda-dashboard", "log-aggregation", "log-collector-dashboard", "log-monitoring-dashboard",
    "logging-configuration", "machine-learning-dashboard", "machine-learning-models",
    "metrics-collector", "metrics-monitoring", "monitoring-dashboard", "network-monitoring",
    "network-traffic", "node-health", "oauth-dashboard", "observability-dashboard",
    "operation-logs", "operations-dashboard", "operator-management", "orchestration-dashboard",
    "pipeline-dashboard", "pipeline-management", "platform-dashboard", "platform-management",
    "policy-dashboard", "policy-management", "process-monitoring", "profiling-dashboard",
    "prometheus-dashboard", "release-dashboard", "release-management", "repository-management",
    "resource-allocation", "resource-monitoring", "rollback-dashboard", "rollback-management",
    "runtime-environment", "saml-dashboard", "sandbox-management", "secret-management-dashboard",
    "security-dashboard", "service-dashboard", "service-mesh-dashboard", "service-monitoring",
    "service-registry", "service-tracing-dashboard", "session-management", "session-monitoring",
    "settings-dashboard", "shared-resources", "shell-dashboard", "slack-dashboard",
    "source-code-management", "source-repository-management", "sso-dashboard", "staging-dashboard",
    "storage-management", "system-dashboard", "system-monitoring", "task-management",
    "testing-dashboard", "third-party-dashboard", "threat-monitoring", "tls-dashboard",
    "token-management-dashboard", "traffic-dashboard", "transaction-dashboard",
    "transit-encryption-dashboard", "tracing-dashboard", "trigger-management", "ui-dashboard",
    "user-management-dashboard", "user-permissions", "version-management", "vulnerability-dashboard",
    "webhook-dashboard", "workflow-dashboard", "workflow-management", "yaml-management",

    # > utilities
    "aboutus", "advertise", "ads", "advertisement", "affiliate", "alerts", "app", "apps", "archive", "archives",
    "articles", "authors", "autosave", "backup", "banners", "beta", "billing", "bookmarks", "bugs", "cache",
    "calendar", "campaigns", "categories", "cdn", "certificates", "chat", "clients", "code", "community",
    "contact-us", "contacts", "copyright", "courses", "credits", "dashboard", "data", "databases", "delivery",
    "developers", "docs", "downloads", "ebooks", "edit", "editor", "email", "emails", "errorpages", "events",
    "export", "faq", "features", "files", "forum", "forums", "friends", "gallery", "galleries", "games", "geo",
    "giftcards", "groups", "helpdesk", "history", "home", "hosting", "icons", "images", "index", "info", "inbox",
    "install", "invoices", "jobs", "language", "languages", "latest", "legal", "license", "link", "links",
    "list", "live", "logs", "login", "logout", "mail", "mailinglist", "maintenance", "marketing", "media",
    "members", "messages", "metrics", "mobile", "mod", "mods", "modules", "news", "newsletters", "notifications",
    "oauth", "offline", "online", "orders", "payments", "pdf", "permissions", "plans", "plugins", "policy",
    "portals", "posts", "pricing", "privacy", "products", "profiles", "projects", "promotions", "public",
    "purchase", "ratings", "react", "reports", "resources", "rss", "sales", "scripts", "search", "security",
    "server", "settings", "shop", "shoppingcart", "signin", "signup", "sitemap", "skills", "social", "software",
    "sponsors", "staff", "stats", "statistics", "status", "store", "subscribers", "subscriptions", "support",
    "system", "tags", "teams", "terms", "testimonials", "themes", "tools", "tour", "tracking", "translations",
    "tutorials", "tv", "uninstall", "unsubscribe", "uploads", "users", "video", "videos", "vip", "voice",
    "web", "webmaster", "widgets", "wiki", "wordpress", "www", "www-data", "xhtml", "xml", "xmlrpc.php", "youtube",
    "zip",
])

def check_path(base_url, path):
    url = f"{base_url.rstrip('/')}/{path}"
    try:
        response = requests.get(url, timeout=6)
        return url, response.status_code
    except requests.RequestException:
        return url, None

def main():
    base_url = input("Enter the base website URL (e.g., https://example.com): ").strip()
    print("Please wait while we scan... This might take a while.\n")

    green_results = []
    yellow_results = []
    red_results = []

    for path in PATHS:
        url, status = check_path(base_url, path)
        if status == 200:
            green_results.append(f"{Fore.GREEN}[FOUND] {url} (Status: {status}){Style.RESET_ALL}")
        elif status is not None:
            yellow_results.append(f"{Fore.YELLOW}[{status}] {url}{Style.RESET_ALL}")
        else:
            red_results.append(f"{Fore.RED}[ERROR] {url}{Style.RESET_ALL}")

    for line in sorted(green_results):
        print(line)
    for line in sorted(yellow_results):
        print(line)
    for line in sorted(red_results):
        print(line)

if __name__ == "__main__":
    main()

# If you have any questions or need help, please contact me on Discord: @daleconner1960

# This tool is for educational purposes only. Do not use it for any illegal activities.

# I am not responsible for any damage caused by this tool. Use it at your own risk.

# This tool is not affiliated with any organization or company.

# This tool is open source and free to use. You can modify it as you wish.
