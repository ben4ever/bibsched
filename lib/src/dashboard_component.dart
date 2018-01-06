import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';

@Component(
  selector: 'dashboard',
  templateUrl: 'dashboard_component.html',
  directives: const [
    materialDirectives,
    CORE_DIRECTIVES,
  ],
)
class DashboardComponent {}
